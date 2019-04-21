
# RTC

https://www.youtube.com/watch?v=9aN2ocO2AWY





https://www.raspberrypi-spy.co.uk/2015/05/adding-a-ds3231-real-time-clock-to-the-raspberry-pi/


https://github.com/skiselev/rpi_rtc_ds3231

```
Enable Kernel Support for DS3231 RTC

Open /boot/config.txt in your favorite editor (nano, vi) as root. For example:

$ sudo nano /boot/config.txt
Add the following lines at the end of the file:

# Enable DS3231 RTC
dtoverlay=i2c-rtc,ds3231
Remove fake-hwclock package:

$ sudo apt-get -y remove fake-hwclock
$ sudo update-rc.d -f fake-hwclock remove
Enable setting up system time to the RTC time at boot. Open /lib/udev/hwclock-set in your favorite editor:

$ sudo nano /lib/udev/hwclock-set
And comment out the following lines:

#if [ -e /run/systemd/system ] ; then
# exit 0
#fi

```







http://www.intellamech.com/RaspberryPi-projects/rpi_RTCds3231

```
Load the clock at boot
sudo nano /etc/rc.local
Add the following lines before exit 0
echo ds1307 0x68 > /sys/class/i2c-adapter/i2c-1/new_device
hwclock -s
Reboot
```