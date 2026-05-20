#SvxLink for Nanopi-neo and the Repeater-Builders.com "NanoPi-Neo Hat"
(images/nanopi-neo.jpg)      (images/svxlink_logo.png) 


Thanks to Tobias Blömberg SM0SVX for the SvxLink Software

The image associated with this repository is found in 'Releases' on the right of this page. Simply download the image and install it on a 16 Gb microSD card using an image builder of your choice.

Under normal circumstances, the image should not need to be unzipped (as happens with the Raspberry Pi Imager)

Install into the NanoPi-Neo with the hat in place. Follow the instruction with the hat to connect your transceiver or transceivers/repeater hardware.

Avoid using a Yaesu DR1X or DR2X as you will not achieve the benefit of the Repeater Configuration of the software, unless you disable the onboard hardware of the repeater.

Connect the Nanopi-Neo to your IP Network before powering up, then do so.

Go to a browser on a computer within the same IP network and enter svxlink.local:5000 and you can then begin the configuration.

Pay special attention to your hardware's configuration, particularly the operation of the Squelch (SQL/COS) and the PTT. Under normal circumstances these will both be Active High. But in the eventuality of a difference, both of these can be individually changed to Active Low by going back to the relevant page in the software.





