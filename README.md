<h2>SvxLink for Nanopi-neo and the Repeater-Builder.com "NanoPi-Neo HAT"</h2><br>
<p align = "center">
<img src="images/nanopi-neo.jpeg" width="400">
<br>
Thanks to Tobias Blömberg SM0SVX for the SvxLink Software now on version 26.05.1 with several security updates.<br>
</p>
<p align = center>
<img src="images/svxlink_logo.png" width="200"><br>
</p>
<p>The image associated with this repository is found in 'Releases' on the right of this page. Simply download the image and install it on a 16 Gb microSD card using an image builder of your choice.<br></p>
<p>Here is the link to the download :[https://github.com/f5vmr/svx-nanopi/releases/download/V26.05.1_Armbian/svxlink_26.05.1_armbian.img.gz]
</p>
Under normal circumstances, the image should not need to be unzipped (as also happens with the Raspberry Pi Imager 1.9.6 - a raspberry pi image remains zipped and the imager unzips it for you. Use 2.10.1 of the RaspberryPi Imager or its Armbian euivalent found here https://imager.armbian.com/.)
<p> While Armbian OS 13 equivalent is available, it is untried and untested. This SvxLink image is constructed on Armbian Jammy a version of Ubuntu that has long term support. Upgrading the OS will serve no purpose.</p>
<pre>PRETTY_NAME="Armbian 26.2.1 jammy"
NAME="Ubuntu"
VERSION_ID="22.04"
VERSION="22.04.5 LTS (Jammy Jellyfish)"
VERSION_CODENAME=jammy
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.armbian.com/"
SUPPORT_URL="https://forum.armbian.com"
BUG_REPORT_URL="https://www.armbian.com/bugs"
PRIVACY_POLICY_URL="https://www.armbian.com"
UBUNTU_CODENAME=jammy
ARMBIAN_PRETTY_NAME="Armbian 26.2.1 jammy"</pre>

<p>Install into the NanoPi-Neo with the hat in place. Follow the instruction with the hat to connect your transceiver or transceivers/repeater hardware. The Nanopi-Neo with the HAT requires no other hardware, it has an on-board sound card and GPIOD configuration prepared for this configuration. Be aware that you will be asked questions in the menu. You shall need to know the actions of your radio equipment with regard to PTT and COS. In general terms PTT is activated by dragging the PTT line to ground - Active-Low. In the main when a signal is received by the radio equipment a high signal is detected at COS - Active High.<br>
Because this image already contains the parameters for PTT, you will only be asked for the SQL setting. This can be GPIOD or CTCSS. Generally if both are set then it will work primarily on GPIOD. So if CTCSS is requires set it alone.<br>
CTCSS for SvxLink is combined with the incoming audio not on a separate line.</p>
<p>If you wish to join the SvxReflector  https://north.america.svxlink.net, then click on the downloads link and join SvxLink to register, and a password will be emailed to you, to complete the menu.</p>

<p>Avoid using a Yaesu DR1X or DR2X as you will not achieve the benefit of the Repeater Configuration of the software, unless you disable the onboard hardware of the repeater. This will defeat the Digital repeater, leaving it on FM Analog only. If you wish to retain the digital mode, then run svxlink as simplex, but you will need to learn more about the settings.</p>

<p>Connect the Nanopi-Neo to your IP Network before powering up, then turn it on.</p>

<p>Go to a browser on a computer within the same IP network and enter svxlink.local:5000 and you can then begin the configuration.</p>

<p> Remember pay special attention to your hardware's configuration, particularly the operation of the Squelch (SQL/COS) and the PTT. Under normal circumstances these will both be Active High and Active Low respectively. But in the eventuality of a difference, the receive can be changed to Active Low by going back to the relevant page in the software menu.</p>
<br>
<img src="images/1.png" width="200"><img src="images/2.png" width="200"><img src="images/3.png" width="200"><br>
<img src="images/4.png" width="200"><img src="images/5.png" width="200"><img src="images/6.png" width="200"><br>
<img src="images/7.png" width="200"><img src="images/8.png" width="200"><img src="images/9.png" width="200"><br>
<img src="images/A.png" width="200"><img src="images/B.png" width="200"><img src="images/C.png" width="200"><br>
<img src="images/E.png" width="200"><img src="images/F.png" width="200"><img src="images/G.png" width="200"><br>
<p align = center src="images/G.png" width="200"></p>
<br>
<p align = center>
At the end of the build you shall have one of these....It will always be svxlink.local:5000/status <br>
<p align= center>
<img src="images/I.png">
</p>

<b>and if it all goes wrong .....</b>
<p>So first of all, go to the terminal and log in as user 'pi' and password 'nanopi'.</p>
<p>cd /opt/dashboard</p>
<p>sudo rm config/node_model.json</p>
<p>exit</p>
<p>Now go back to svxlink.local:5000 in the browser and begin again from scratch</p>
<p>If you ever forget your dashboard user and password, then go into the terminal again but this time cd /opt/dashboard/tools/</p>
<p>sudo ./reset_dashboard_auth.py and follow the instruction. You will be required to make a new user and new password, (that can be identical to the originals.</p>
<p>Exit the terminal and go back to svxlink.local/status which is where you probably want to be.</p>
<p>If you need to know more, or do more with SvxLink, then at the terminal type 'man svxlink.conf' which is the fount of all knowledge. If you are still stuck then, go to https://groups.io/svxlink and research there. To meet others in the SvxLink community, then you can go to Facebook SvxLink Amateur Radio Users.</p

<p>This project cannot provide you with all the answers, as the SvxLink software is far too deep to explain simply.</p>

<p>If you really want to know more then go to svxlink.org, the very heart of the project.</p>
<p><b>Interface</b></p>
<img align=center src="images/Nanopi-neo-interface.jpg" width="600"><br>
<p><b>Special Note regarding Audio Level and alsamixer/amixer</b>.<br>
While every effort has been made to set the audio levels to a reasonable state, there will be reasons for change dependant on the equipment used. The potentiometer in the NanoPi-Neo Repeater-Builder hat should be set initially at the midway position. While there are opportunity for change of the audio settings, make a record of the initial settings before changing them.<br>
<pre>
### H3 codec mixer state
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
</pre>

<p>Again thanks go to Tobias Blömberg SM0SVX and the team of developers, that have brought this fine project to the Amateur Radio Community.</p>

<p>Thanks to Scott Zimmerman N3XCC for his enthusiasm and support for this project.</p>

<p>73 from Chris G4NAB (formerly F5VMR) developer of the Svxlink Dashboard V3.1</p>

