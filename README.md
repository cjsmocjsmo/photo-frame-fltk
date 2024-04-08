To run this you need to install:

sudo apt install python3-pil
sudo apt install python3-pil.imagetk

Fltk should already be installed on the RaspberrypiOS already.

When running on the Pi Pico you will need to increase the swapfile size. Do this first or you will have problems.
Edit the file /etc/dphys-swapfile

Look for the section:
CONF_SWAPSIZE=100

Increase it to the desire amount of new swap for example
CONF_SWAPSIZE=1023

Save and reboot.
