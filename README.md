

# Installation

## Clone Repository

```
git clone https://github.com/SebPez/TimelapseRPi.git
```

## Add script to Raspberry Boot


```
sudo nano /etc/rc.local
```

Then add 


```
#Run Timelapse Script
python /home/pi/TimelapseRPi/timelapse.py  &
```

Above ```exit 0```.

**WARNING**: 

Since the script runs an infinite loop, you must be sure to fork the process by adding an ampersand (```&```) to the end of the command.

The ampersand allows the command to run in a separate process and continue booting with the process running.

_____

# gphoto2-updater

This script allows to install last development and last stable releases of gphoto2 and libgphoto2.

```
wget https://raw.githubusercontent.com/gonzalo/gphoto2-updater/master/gphoto2-updater.sh && chmod +x gphoto2-updater.sh && sudo ./gphoto2-updater.sh
```

_____

#  Auto-Mount Issue

Fix for Nikon D3200

```
sudo chmod -x /usr/lib/gvfs/gvfs-gphoto2-volume-monitor
```

_____


# Cloning SD - Recommended way

https://etcher.io


## Source SD Card
Showing Disk list.
```
diskutil list
```

Copying ***from*** SD Card

```
sudo dd if=/dev/disk2 of=/Users/<user>/Desktop/timelapse_raspbian_stretch.dmg
```


## Destination SD Card

```
diskutil unmountDisk /dev/disk2
```

Cloning into new SD Card
```
sudo dd if=/Users/<user>/Desktop/timelapse_raspbian_stretch.dmg of=/dev/disk2
```

_____

## Recommended Raspbian Version

### **Raspbian Stretch With Desktop**

Image with desktop based on Debian Stretch

**Version:** June 2018

**Release date:** 2018-06-27

_____

## Documentation

https://github.com/gonzalo/gphoto2-updater

https://www.raspberrypi.org/documentation/linux/usage/rc-local.md

https://computers.tutsplus.com/articles/how-to-clone-raspberry-pi-sd-cards-using-the-command-line-in-os-x--mac-59911







_____

# RTC
http://www.intellamech.com/RaspberryPi-projects/rpi_RTCds3231
https://github.com/skiselev/rpi_rtc_ds3231

```
Enable kernel support
sudo raspi-config.
Choose Advanced Options then I2C and select yes to enable the interface.



//
Enable Kernel Support for DS3231 RTC

Open /boot/config.txt in your favorite editor (nano, vi) as root. For example:

$ sudo nano /boot/config.txt
Add the following lines at the end of the file:

# Enable DS3231 RTC
dtoverlay=i2c-rtc,ds3231

```

