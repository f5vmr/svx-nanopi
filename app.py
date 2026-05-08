from flask import Flask, render_template, request, redirect, send_from_directory
import grp
import os
import pwd
import re
import shutil
from collections import OrderedDict

app = Flask(__name__)
# In production, the read-only base configuration is at /etc/svxlink/svxlink.orig
# The live configuration file is written to /etc/svxlink/svxlink.conf.
# Permissions on that location should be svxlink:svxlink with mode 0765.
CONFIG_FILE = '/etc/svxlink/svxlink.conf'
ORIG_CONFIG_FILE = '/etc/svxlink/svxlink.orig'
ECHOLINK_CONFIG_FILE = '/etc/svxlink/svxlink.d/ModuleEchoLink.conf'
METAR_CONFIG_FILE = '/etc/svxlink/svxlink.d/ModuleMetarInfo.conf'
EVENT_SOURCE_DIR = '/usr/share/svxlink/events.d'
EVENT_DEST_DIR = '/usr/share/svxlink/events.d/local'
EVENT_FILES = ['Logic.tcl', 'RepeaterLogicType.tcl']
# Standard CTCSS frequencies
CTCSS_FREQUENCIES = [
    67.0, 69.3, 71.9, 74.4, 77.0, 79.7, 82.5, 85.4, 88.5, 91.5, 94.8, 97.4, 100.0,
    103.5, 107.2, 110.9, 114.8, 118.8, 123.0, 127.3, 131.8, 136.5, 141.3, 146.2, 151.4,
    156.7, 159.8, 162.2, 167.9, 173.8, 179.9, 186.2, 192.8, 203.5, 210.7, 218.1, 225.7,
    233.6, 241.8, 250.3
]

def validate_callsign(callsign):
    callsign = callsign.strip().upper()
    if not callsign:
        return False
    if callsign in ('-L', '-R'):
        return False
    if callsign.startswith('-'):
        return False
    if re.search(r'\s', callsign):
        return False
    if not re.match(r'^[A-Z0-9/]+$', callsign):
        return False
    return True



def parse_config(filename):
    if filename == CONFIG_FILE and not os.path.exists(filename) and os.path.exists(ORIG_CONFIG_FILE):
        filename = ORIG_CONFIG_FILE
    
    preamble = []
    sections = OrderedDict()
    current_section = None

    try:
        f = open(filename, 'r')
    except PermissionError:
        if filename == CONFIG_FILE and os.path.exists(ORIG_CONFIG_FILE):
            filename = ORIG_CONFIG_FILE
            f = open(filename, 'r')
        else:
            raise

    with f:
        for line in f:
            raw = line.rstrip('\n')
            stripped = raw.strip()

            if stripped.startswith('[') and stripped.endswith(']'):
                current_section = stripped[1:-1]
                sections[current_section] = {'items': [{'type': 'header', 'raw': raw}]}
            elif current_section is None:
                preamble.append({'type': 'raw', 'raw': raw})
            else:
                if stripped == '':
                    sections[current_section]['items'].append({'type': 'blank', 'raw': raw})
                elif '=' in stripped:
                    if stripped.startswith('#'):
                        key, value = stripped[1:].split('=', 1)
                        sections[current_section]['items'].append({
                            'type': 'kv',
                            'enabled': False,
                            'key': key.strip(),
                            'value': value.strip(),
                            'raw': raw,
                        })
                    else:
                        key, value = stripped.split('=', 1)
                        sections[current_section]['items'].append({
                            'type': 'kv',
                            'enabled': True,
                            'key': key.strip(),
                            'value': value.strip(),
                            'raw': raw,
                        })
                else:
                    sections[current_section]['items'].append({'type': 'comment', 'raw': raw})

    return {'preamble': preamble, 'sections': sections}


def serialize_config(config):
    lines = []
    for item in config['preamble']:
        lines.append(item['raw'])

    if config['preamble']:
        lines.append('')

    for section_name, section_data in config['sections'].items():
        for item in section_data['items']:
            if item['type'] == 'header':
                lines.append(item['raw'])
            elif item['type'] == 'blank':
                lines.append(item['raw'])
            elif item['type'] == 'comment':
                lines.append(item['raw'])
            elif item['type'] == 'kv':
                if item['enabled']:
                    lines.append(f"{item['key']}={item['value']}")
                else:
                    lines.append(f"#{item['key']}={item['value']}")

    return '\n'.join(lines).rstrip() + '\n'


def ensure_local_event_dir():
    os.makedirs(EVENT_DEST_DIR, exist_ok=True)


def sync_event_files():
    ensure_local_event_dir()
    for filename in EVENT_FILES:
        src = os.path.join(EVENT_SOURCE_DIR, filename)
        dst = os.path.join(EVENT_DEST_DIR, filename)
        if os.path.exists(src):
            shutil.copy2(src, dst)


def modify_logic_tcl(tone_type, tone_freq=None):
    """
    Modify Logic.tcl in the local events directory based on courtesy tone selection.
    Always comment out the CW::play line and modify the playTone line based on tone_type.
    """
    logic_tcl_path = os.path.join(EVENT_DEST_DIR, 'Logic.tcl')
    
    if not os.path.exists(logic_tcl_path):
        return
    
    with open(logic_tcl_path, 'r') as f:
        content = f.read()
    
    # Always comment out the CW::play line
    content = content.replace(
        'CW::play $sql_rx_id 200 1000 -10',
        '# CW::play $sql_rx_id 200 1000 -10'
    )
    
    # Modify the playTone line based on tone_type
    if tone_type == 'none':
        # Comment out playTone for no tone
        content = content.replace(
            'playTone 440 500 100',
            '# playTone 440 500 100'
        )
    elif tone_type == 'beep':
        # Replace with beep using frequency and duration, volume 60
        # Default: 800 Hz, 800 ms
        freq = tone_freq if tone_freq else '800'
        duration = '800'
        content = content.replace(
            'playTone 440 500 100',
            f'playTone {freq} {duration} 60'
        )
    elif tone_type == 'morse_t':
        # Replace with Morse code T
        content = content.replace(
            'playTone 440 500 100',
            'CW::play "T"'
        )
    elif tone_type == 'morse_k':
        # Replace with Morse code K
        content = content.replace(
            'playTone 440 500 100',
            'CW::play "K"'
        )
    
    with open(logic_tcl_path, 'w') as f:
        f.write(content)


def set_config_permissions(filename):
    try:
        uid = pwd.getpwnam('svxlink').pw_uid
        gid = grp.getgrnam('svxlink').gr_gid
        try:
            os.chown(filename, uid, gid)
        except PermissionError:
            pass
    except KeyError:
        pass

    try:
        os.chmod(filename, 0o640)
    except PermissionError:
        pass


def save_config(filename, config):
    with open(filename, 'w') as f:
        f.write(serialize_config(config))
    if filename == CONFIG_FILE:
        set_config_permissions(filename)


def restore_backup(filename):
    if os.path.exists(ORIG_CONFIG_FILE):
        if os.path.exists(filename):
            os.remove(filename)
        shutil.copy(ORIG_CONFIG_FILE, filename)
        if filename == CONFIG_FILE:
            set_config_permissions(filename)
        return True
    return False


def get_section(config, section_name, create=False):
    if section_name not in config['sections']:
        if not create:
            return None
        config['sections'][section_name] = {'items': [{'type': 'header', 'raw': f'[{section_name}]'}]}
    return config['sections'][section_name]


def find_kv(section, key):
    for item in section.get('items', []):
        if item['type'] == 'kv' and item['key'] == key:
            return item
    return None


def set_kv(config, section_name, key, value, enabled=True):
    section = get_section(config, section_name, create=True)
    item = find_kv(section, key)
    if item:
        item['value'] = value
        item['enabled'] = enabled
    else:
        section['items'].append({
            'type': 'kv',
            'enabled': enabled,
            'key': key,
            'value': value,
            'raw': None,
        })


def set_section_enabled(config, section_name, enabled):
    section = get_section(config, section_name, create=False)
    if not section:
        return
    for item in section['items']:
        if item['type'] == 'kv':
            item['enabled'] = enabled


def replace_callsign(config, old_callsign, new_callsign):
    for section in config['sections'].values():
        for item in section['items']:
            if item['type'] == 'kv' and old_callsign in item['value']:
                item['value'] = item['value'].replace(old_callsign, new_callsign)


def ensure_comma_value(config, section_name, key, new_piece):
    section = get_section(config, section_name, create=True)
    item = find_kv(section, key)
    if item:
        values = [v.strip() for v in item['value'].split(',') if v.strip()]
        if new_piece not in values:
            values.append(new_piece)
            item['value'] = ','.join(values)
        item['enabled'] = True
    else:
        section['items'].append({
            'type': 'kv',
            'enabled': True,
            'key': key,
            'value': new_piece,
            'raw': None,
        })


def uncomment_kv(config, section_name, key, value=None):
    section = get_section(config, section_name, create=True)
    item = find_kv(section, key)
    if item:
        item['enabled'] = True
        if value is not None:
            item['value'] = value
    else:
        section['items'].append({
            'type': 'kv',
            'enabled': True,
            'key': key,
            'value': value if value is not None else '',
            'raw': None,
        })


@app.route('/')
def index():
    return redirect('/setup')


@app.route('/css/<path:filename>')
def css_file(filename):
    return send_from_directory(os.path.join(app.root_path, 'css'), filename, mimetype='text/css')


@app.route('/images/<path:filename>')
def image_file(filename):
    return send_from_directory(os.path.join(app.root_path, 'images'), filename)


@app.route('/setup', methods=['GET', 'POST'])
def setup():
    error = None
    node_type = 'simplex'
    tone_type = 'none'
    tone_freq = '800'
    squelch_method = 'gpiod'
    ctcss_freq = '100.0'
    ctcss_tx = 'no'

    if request.method == 'POST':
        node_type = request.form.get('node_type', 'simplex')
        callsign = request.form.get('callsign', '').strip().upper()
        tone_type = request.form.get('tone_type', 'none')
        tone_freq = request.form.get('tone_freq', '800').strip()
        squelch_method = request.form.get('squelch_method', 'gpiod')
        ctcss_freq = request.form.get('ctcss_freq', '100.0').strip()
        ctcss_tx = request.form.get('ctcss_tx', 'no')

        if not validate_callsign(callsign):
            error = 'Enter a valid standard callsign; do not use -L or -R.'
        elif tone_type not in ('none', 'beep', 'morse_t', 'morse_k'):
            error = 'Please select a valid courtesy tone option.'
        elif tone_type == 'beep':
            try:
                freq_value = int(tone_freq)
                if not 600 <= freq_value <= 1000:
                    error = 'Beep frequency must be between 600 and 1000 Hz.'
            except ValueError:
                error = 'Beep frequency must be a number between 600 and 1000.'
        elif squelch_method not in ('gpiod', 'ctcss'):
            error = 'Please select a valid squelch method.'
        elif squelch_method == 'ctcss':
            try:
                ctcss_value = float(ctcss_freq)
                if ctcss_value not in CTCSS_FREQUENCIES:
                    error = 'Please select a valid CTCSS frequency from the list.'
            except ValueError:
                error = 'CTCSS frequency must be a number.'
            if ctcss_tx not in ('yes', 'no'):
                error = 'Please specify if CTCSS is for receive only or transmit and receive.'
        else:
            freq_value = 800

        if error is None:
            config = parse_config(CONFIG_FILE)

            logic_section = 'SimplexLogic' if node_type == 'simplex' else 'RepeaterLogic'

            if node_type == 'simplex':
                set_kv(config, 'GLOBAL', 'LOGICS', 'SimplexLogic', enabled=True)
                set_kv(config, 'ReflectorLogic', 'CONNECT_LOGICS', 'SimplexLogic', enabled=True)
                set_kv(config, 'ReflectorLink', 'CONNECT_LOGICS', 'SimplexLogic:9,ReflectorLogic', enabled=True)
                set_section_enabled(config, 'SimplexLogic', True)
                set_section_enabled(config, 'RepeaterLogic', False)
                set_kv(config, 'SimplexLogic', 'CALLSIGN', callsign, enabled=True)
            elif node_type == 'repeater':
                set_kv(config, 'GLOBAL', 'LOGICS', 'RepeaterLogic', enabled=True)
                set_kv(config, 'ReflectorLogic', 'CONNECT_LOGICS', 'RepeaterLogic', enabled=True)
                set_kv(config, 'ReflectorLink', 'CONNECT_LOGICS', 'RepeaterLogic:9,ReflectorLogic', enabled=True)
                set_section_enabled(config, 'RepeaterLogic', True)
                set_section_enabled(config, 'SimplexLogic', False)
                set_kv(config, 'RepeaterLogic', 'CALLSIGN', callsign, enabled=True)

            # Set squelch
            if squelch_method == 'gpiod':
                # GPIOD is the default Rx1 squelch method, no config changes needed here.
                pass
            elif squelch_method == 'ctcss':
                # For CTCSS alone, modify Rx1 section directly
                set_kv(config, 'Rx1', 'SQL_DET', 'CTCSS', enabled=True)
                set_kv(config, 'Rx1', 'CTCSS_MODE', '4', enabled=True)
                set_kv(config, 'Rx1', 'CTCSS_FQ', ctcss_freq, enabled=True)

                # Comment out GPIO lines when switching to CTCSS only
                set_kv(config, 'Rx1', 'SQL_GPIOD_CHIP', 'gpiochip0', enabled=False)
                set_kv(config, 'Rx1', 'SQL_GPIOD_LINE', '!203', enabled=False)

                # If transmit and receive, also modify Tx1 section
                if ctcss_tx == 'yes':
                    set_kv(config, 'Tx1', 'CTCSS_FQ', ctcss_freq, enabled=True)
                    set_kv(config, 'Tx1', 'CTCSS_LEVEL', '-24', enabled=True)

            replace_callsign(config, 'MYCALL', callsign)

            if tone_type == 'beep':
                tone_value = f'BEEP,{freq_value}Hz,800ms'
            elif tone_type == 'morse_t':
                tone_value = 'MORSE,T'
            elif tone_type == 'morse_k':
                tone_value = 'MORSE,K'
            else:
                tone_value = 'NONE'

            #set_kv(config, 'GLOBAL', 'COURTESY_TONE', tone_value, enabled=True)

            save_config(CONFIG_FILE, config)
            sync_event_files()
            modify_logic_tcl(tone_type, tone_freq)
            return redirect('/connect')

    return render_template('setup.html', error=error, node_type=node_type, tone_type=tone_type, tone_freq=tone_freq, squelch_method=squelch_method, ctcss_freq=ctcss_freq, ctcss_tx=ctcss_tx, ctcss_frequencies=CTCSS_FREQUENCIES)


@app.route('/connect', methods=['GET', 'POST'])
def connect():
    error = None
    if request.method == 'POST':
        answer = request.form.get('connect')
        password = request.form.get('password', '').strip()
        config = parse_config(CONFIG_FILE)

        if answer == 'yes':
            if not password:
                error = 'Please enter the 16-character subscription password from north.america.svxlink.net.'
            elif len(password) != 16:
                error = 'Password must be exactly 16 characters long.'
            else:
                set_kv(config, 'ReflectorLogic', 'HOSTS', 'north.america.svxlink.net', enabled=True)
                uncomment_kv(config, 'GLOBAL', 'LINKS', 'ReflectorLink')
                ensure_comma_value(config, 'GLOBAL', 'LOGICS', 'ReflectorLogic')
                set_kv(config, 'ReflectorLogic', 'AUTH_KEY', password, enabled=True)
                save_config(CONFIG_FILE, config)
                sync_event_files()
                return redirect('/done')
        else:
            return redirect('/done')

    return render_template('connect.html', error=error)


@app.route('/done')
def done():
    return render_template('done.html')

@app.route('/talkgroup')
def talkgroup():
    return render_template('talkgroup.html')

@app.route('/reflector')
def reflector():
    return render_template('reflector.html')

@app.route('/echolink')
def echolink():
    return render_template('echolink.html')

@app.route('/metar')
def metar():
    return render_template('metar.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/advanced')
def advanced(): 
    return render_template('advanced.html')

@app.route('/restart', methods=['POST'])
def restart():
    restore_backup(CONFIG_FILE)
    return redirect('/setup')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)