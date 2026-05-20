<h2>SvxLink for Nanopi-neo and the Repeater-Builders.com "NanoPi-Neo Hat"</h2><br>
<p align = "center">
<img src="images/nanopi-neo.jpeg" width="400">
<br>
Thanks to Tobias Blömberg SM0SVX for the SvxLink Software<br>
</p>
<p align = center>
<img src="images/svxlink_logo.png" width="200"><br>
</p>
<br>The image associated with this repository is found in 'Releases' on the right of this page. Simply download the image and install it on a 16 Gb microSD card using an image builder of your choice.<br>
<p>Here is the link to the download : https://github.com/f5vmr/svx-nanopi/releases/download/V1.0/svx-nanopi-neo.img.gz </p>
Under normal circumstances, the image should not need to be unzipped (as happens with the Raspberry Pi Imager)

Install into the NanoPi-Neo with the hat in place. Follow the instruction with the hat to connect your transceiver or transceivers/repeater hardware.

Avoid using a Yaesu DR1X or DR2X as you will not achieve the benefit of the Repeater Configuration of the software, unless you disable the onboard hardware of the repeater.

Connect the Nanopi-Neo to your IP Network before powering up, then do so.

Go to a browser on a computer within the same IP network and enter svxlink.local:5000 and you can then begin the configuration.

Pay special attention to your hardware's configuration, particularly the operation of the Squelch (SQL/COS) and the PTT. Under normal circumstances these will both be Active High. But in the eventuality of a difference, both of these can be individually changed to Active Low by going back to the relevant page in the software.
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
<p>Now go back to svxlink.local:5000 and start again</p>
<p>If you ever forget your dashboard user and password, then go into the terminal again but this time cd /opt/dashboard/tools/</p>
<p>sudo ./reset_dashboard_auth.py and follow the instruction.</p>
<p>Exit the terminal and go back to svxlink.local/status which is where you probably want to be.</p>
<p>If you need to know more, or do more with SvxLink, then at the terminal type 'man svxlink.conf' which is the fount of all knowledge. If you are still stuck then, go to https://groups.io/svxlink and research there. To meet others in the SvxLink community, then you can go to Facebook SvxLink Amateur Radio Users.</p

<p>This project cannot provide you with all the answers, as the SvxLink software is far too deep to explain simply.</p>

<p>If you really want to know more the go to svxlink.org, the very heart of the project.</p>

<p>Again thanks go to Tobias Blömberg SM0SVX and the team of developers, that have brought this fine project to the Amateur Radio Community.</p>

<p>Thanks to Scott Zimmerman N3XCC for his enthusiasm and support for this project.</p>

<p>73 from Chris G4NAB (formerly F5VMR)</p>

