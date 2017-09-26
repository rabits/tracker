Tracker
=======

Car media system that allow to listen bluetooth music, track car via GPS and manage car cameras

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

### No graphics interface

Will save some battery, cpu & some memory

### Read only root

Will save your sdcard & data on accidental poweroff

### Watchdog

Will reboot raspberry pi on stuck

Platforms
---------

### Raspberry PI 3

#### Power

* Default: 230mA
* Maximum: 650mA
* Powered Off: 100mA

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

* bluealsa - to provide blueatooth audio service
  * bluealsa-aplay "connected device address" - connecting bluetooth media device to default soundcard
