Tracker
=======

Car media system that allow to listen bluetooth music, track car via GPS and manage car cameras

Requirements
------------
* python2.7
* python-yaml
* python-dbus
* python-bluez
* python-serial
* python-smbus

States
------

### Default - sleep

By default with turned off ignition:

1. LAN & USB disabled
2. Bluetooth disabled
3. WiFi in Client mode and trying to find/connect to known SSIDs
4. Using GSM & GPS systems until connection to WiFi
4. If WiFi is connected & connection is ok:
  * GSM data & GPS disabled

### Wake

When you turn on the ignition, Tracker will:

1. Enable LAN & USB
2. Enable Bluetooth
3. Switch WiFi to Ad-Hoc mode
4. Enable GSM data & GPS

Nice To Have
------------

### Read only root

Will save your sdcard & data on accidental poweroff

### Watchdog

Will reboot raspberry pi on stuck

Hardware
--------

### Raspberry PI 3

#### Power

* Default: 230mA
* Maximum: 650mA
* Powered Off: 100mA
* Bluetooth music playing: 240-290mA

##### Optimizations

* Disabled LAN & USB: -60mA
```
echo 0 | sudo tee /sys/devices/platform/soc/3f980000.usb/buspower
echo 1 | sudo tee /sys/devices/platform/soc/3f980000.usb/buspower
```

* Disable HDMI: -20mA
```
sudo /opt/vc/bin/tvservice -o
sudo /opt/vc/bin/tvservice -p
```

* Disable WiFi: -20mA
```
sudo rmmod brcmfmac brcmutil
sudo modprobe brcmfmac brcmutil
```

#### Bluetooth

##### Adapter settings

* AFH Mode: 1
* SSP Mode: 0
* encrypt
* noauth
* piscan

##### Additional software

* bluealsa - to provide blueatooth audio service (Jittery audio due to wifi+bt issue: https://github.com/Arkq/bluez-alsa/issues/60)
  * bluealsa-aplay "connected device address" - connecting bluetooth media device to default soundcard

### GSM/GPS SIM5320A

It is possible to connect gsm and gps module to track your position and have persistent internet connection.
This one was tested with "DIYMall SIM5320A 3G GSM GPRS GPS Expansion Board WCDMA + HSDPA" - but any GSM module could be adapted.

#### Power

* GSM board enabled: +60mA
* GPS enabled: +30mA

#### Configuration

Additional configuration is required to enable communication channel between rpi & module.
HW UART ttyAMA0 still will be used by bluetooth (and it's good, we need a strong connection) and we can use ttyS0 to interact with our GSM module.

* /boot/config.txt
```
# Enabling mini uart to rule the GSM module
enable_uart=1 # Now UART GPIO pins (GPIO14, GPIO15) will be used by miniUART
core_freq=250 # Required to have constant baud rates
```

### OBD1 ALDL-USB Cable 1320 Electronics

Check ALDL160 [README](doc/ALDL_160baud/README.md) for more info

### ADS1115 via I2C

Checking input voltage requires at lease one Analog-Digital Converter.

Simple voltage divider (~1/10) and zener diode used to get appropriate value.

TODO
----

* HUD display - hdmi projector + optical system to show picture on the windshield
* TextToSpeech interface & audio notification support - verbal events & status

Support
-------
If you like this project, you can support our open-source development by a small Bitcoin donation.

Bitcoin wallet: `15phQNwkVs3fXxvxzBkhuhXA2xoKikPfUy`

