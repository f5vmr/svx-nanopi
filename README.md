### SvxLink for Nanopi-neo and the Repeater-Builder.com "NanoPi-Neo HAT"
![The NanoPi-Neo Repeater Controller](images/nanopi-neo.jpeg)

**Thanks to Tobias Blömberg SM0SVX for the SvxLink Software now on version 26.05.2 with several security updates.**

![](images/logo.png)

The image associated with this repository is found in 'Releases' on the right of this page. Simply download the image and install it on a 16 Gb microSD card using Armbian Imager and the option **Custom Image**.

https://github.com/f5vmr/svx-nanopi/releases/download/V26.05.1_Armbian/nanopi_neo_svxlink.img.gz



Do not unzip the image as the Armbian Imager will perform this for you.
_This SvxLink image is constructed on Armbian 22.06 Minimal a version of Ubuntu that has long term support. Upgrading the OS will serve no purpose._

Install into the NanoPi-Neo with its hat in place and the radio/repeater powered and connected to a dummy load in the first instance. Follow the instruction with the hat to connect your transceiver or transceivers/repeater hardware. 

The Nanopi-Neo with the HAT requires no other hardware, it has an on-board sound card and GPIOD configuration prepared for this configuration. 

Be aware that you will be asked questions in the menu. You shall need to know the actions of your radio equipment with regard to PTT and COS. In general terms PTT is activated by dragging the PTT line to ground - Active-Low. In the main when a signal is received by the radio equipment a high signal is detected at COS - Active High. This may not always be the case, but the modification is simple.

Because this image already contains the parameters for PTT, you will only be asked for the SQL setting. This can be GPIOD or CTCSS. Generally if CTCSS is unset it will work primarily on GPIOD. So if CTCSS is requires set it alone. The frequency can be set as you proceed through the menu.

_CTCSS for SvxLink is combined with the incoming audio not on a separate line such as in AllStarLink._

You are encouraged to join the SvxReflector  https://north.america.svxlink.net, click on the signup link to register, and a password will be emailed to you, in order to complete the menu. Please have that information available, and assemble all your required data information such as EchoLink, before commencing the build menu. 

For the North America Reflector you will be presented with Federation of Svxlink Reflector - choose this option, then North America from the dropdown list, and the password emailled to you from the sign-up. The following menu instructions will demonstrate.

Avoid using a Yaesu DR1X or DR2X on-board controller as you will not achieve the benefit of the Repeater Configuration of the software, unless you disable the that onboard hardware of the repeater. This will defeat the Digital repeater, leaving it on FM Analog only. If you wish to retain the digital mode, then run svxlink as simplex, but you will need to learn more about the settings.

Connect the Nanopi-Neo to your IP Network before powering up, then turn it on.

### Stage 1
With a suitable IP scanner locate the IP address of the NanoPi-Neo.

Go to a browser on a computer within the same IP network and enter svxlink.local:5000 and you can then begin the configuration.

### Stage 2

Enter a suitable User Name and Password for future use of the Dashboard

![The initial screen - enter an identity and password for future use](images/1.jpg)

We are a Single Channel Node here.
![Select 'Single Channel Node'](images/2.jpg)

Confirmation of the platform.
![Platform Confirmation ](images/3.jpg)

Adding the i2c and Sound Card, that are on the Main Board.
![This screen may already be in black rather than in red in which case click continue](images/4.jpg)
![In the event is is not the click 'reboot'](images/5.jpg)

You should now have this
![You should return to this screen](images/6.jpg)

Now we have come confirmation that all is on course.
The net three screens will confirm the single channel status of the NanoPi-Neo.
![The next screen will confirm you location and time zone](images/10.jpg)
![](images/11.jpg)

We begin to populate the configuration.
![Now the important part, the node status as Repeater or Simplex](images/12.jpg)

The Radio Configuration
![For the NanoPi-Neo GPIOD is required](images/13.jpg)

CTCSS or GPIO
![If you want CTCSS operation it is selected here with the frequency](images/14.jpg)
You can also transmit CTCSS too.

Remember the Activation of the Repeater COS/PTT - Active High or Active Low?
![Normally COS is Active High and PTT is Active Low but can be changed later](images/15.jpg)

Identification of the Repeater.
![Timed announcements can be applied here](images/16.jpg)

You can create a personal announcement and upload it here (or later) for example a club net.
![The file is checked for correctness and stored for use](images/17.jpg)

CW Identification if required.
![CW settings - the first option MUST be -10, It also handles the Courtesy Tones later - I suggest changing 95 for 120](images/18.jpg)

Courtesy Tones
![Courtesy Tone - none or a selected or Morse Characters chosen for their length.](images/19.jpg)

Repeater Tones
![Repeater Tones for the idle time after the last transmission before shut off](images/20.jpg)

Repeater Shutoff Tones
![The shutoff noise - None or biboop or ...-.-](images/21.jpg)

Emergency Repeater Shutoff
![Emergency shutoff in case of interference when you are not at home](images/22.jpg)

Sent by DTMF with suffix 0# shuts off the repeater logic, except the RX, Sent with suffix 1# reinstates Repeater Activity.

Idle Time
![The Idle Time before shut off, Shorten it or lengthen it](images/23.jpg)

The 180 Seconds is judged to be a reasonable length of time of an 'over'. Gives the overtime talker an audible reminder "Timeout" when he drops the PTT. During the period exceeding 180 seconds a regular pip-tone can be heard under the talkers transmission telling others of the exceeeded talk-time.

Module Settings
![The Modules EchoLink and MetarInfo can be set here, or left until later](images/24.jpg)

![EchoLink is self explanatory, there are two pages for MetarInfo](images/25.jpg)
![](images/26.jpg)

The SvxReflector Settings.
![The Reflector Settings enhance the connectivity of the repeater across a huge network on a system of Analog Talkgroup](images/27.jpg)

![The North.america.svxlink.net reflector links to three others](images/28.jpg)
![](images/29.jpg)

Location Settings for SvxReflector and APRS
![Fully completing the NodeInfo page gives you a presence on the SvxReflector and APRS](images/30.jpg)

This page is particularly useful for accurate determination.
![This page will help you to determine your locators accurately](images/31.jpg)
![The next page reviews everything, but you can retun to change items later](images/32.jpg)

Now we are set to build the configuration of the Node/Repeater.
![Now we build the configuration file](images/33.jpg)
![At this point we are nearly ready to launch for the first time](images/34.jpg)

Launched - We have a Dashboard, but there are still things to build.
![The Dashboard - Naturally you have editing rights, and you will need to sign in after leaving it unattended](images/35.jpg)

Most of the parameters can be reconfigured through this menu, in case of earlier mistakes, or experimental setting.
![The Reconfiguration menu takes you to here, where you select the item you wish to change](images/36.jpg)

Analog Talkgroups - You can see the active talkgroups on the https://north.america.svxlink.net Selecting some of these provides you will connectivity.
![You can add talkgroups to monitor](images/37.jpg)

Audio Levels - Probably Alsamixer would be best here, in the terminal.
![You can check your audio levels](images/38.jpg)
![Although you may wish to use alsamixer and experiment with the levels](images/38a.jpg)

FOr accurate determination of yout levels devcal is available.
![The devcal tool is built in but you can use it in the terminal](images/39.jpg)

Adn for restart and shutdown, everything is included.
![For graceful shutdown and recovery](images/40.jpg)

For assitance on these and other Dashboard Functions you may email me

dashboard-support@g4nab.co.uk

For Svxlink issues the svxlink version 26.05.2 is fully explained at man svxlink.conf on a google search. groups.io at svxlink holds most if not all the answers.

Please do not pose Dashboard oriented questions in groups.io, they will not understand.

### Addendum

Remember pay special attention to your hardware's configuration, particularly the operation of the Squelch (SQL/COS) and the PTT. Under normal circumstances these will both be Active High and Active Low respectively. But in the eventuality of a difference, the receive can be changed to Active Low by going back to the relevant page in the software menu.

**At the end of the build you shall have one of these. It will always be http://svxlink.local:5000/status or http://xxx.xxx.xxx.xxx:5000/status. Watch the headings at the top of the page as you progress.

This project cannot possibly provide you with all the answers, as the SvxLink software is far too deep to explain simply.

**If you really want to know more then go to svxlink.org, the very heart of the project.**

### Special Note regarding Audio Level and alsamixer/amixer

While every effort has been made to set the audio levels to a reasonable state, there will be reasons for change dependant on the equipment used. The potentiometer in the NanoPi-Neo Repeater-Builder hat should be set initially at the midway position. While there are opportunity for change of the audio settings, make a record of the initial settings before changing them.

### H3 codec mixer state

```
===== numid=17 =====
numid=17,iface=MIXER,name='Line In Capture Switch'
  ; type=BOOLEAN,access=rw------,values=2
  : values=off,off
===== numid=12 =====
numid=12,iface=MIXER,name='Line In Playback Switch'
  ; type=BOOLEAN,access=rw------,values=2
  : values=off,off
===== numid=15 =====
numid=15,iface=MIXER,name='Mixer Capture Switch'
  ; type=BOOLEAN,access=rw------,values=2
  : values=off,off
===== numid=16 =====
numid=16,iface=MIXER,name='Mixer Reversed Capture Switch'
  ; type=BOOLEAN,access=rw------,values=2
  : values=off,off
===== numid=10 =====
numid=10,iface=MIXER,name='DAC Playback Switch'
  ; type=BOOLEAN,access=rw------,values=2
  : values=on,on
===== numid=4 =====
numid=4,iface=MIXER,name='Line Out Playback Switch'
  ; type=BOOLEAN,access=rw------,values=2
  : values=on,on
===== numid=20 =====
numid=20,iface=MIXER,name='Line Out Source Playback Route'
  ; type=ENUMERATED,access=rw------,values=2,items=2
  ; Item #0 'Stereo'
  ; Item #1 'Mono Differential'
  : values=1,1
```

### Again thanks go to Tobias Blömberg SM0SVX and the team of developers, that have brought this fine project to the Amateur Radio Community.

### Thanks to Scott Zimmerman N3XCC for the manufacture of the board, and his enthusiasm and support for this project.

### 73 from Chris G4NAB (formerly F5VMR) developer of the Svxlink Dashboard V4.1, and the Svxlink-Streamer at the top of the dashboard page.

