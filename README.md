Tracker
=======

Car media system that allow to listen bluetooth music, track car via GPS and manage car cameras

Requirements
------------

Depends on what modules you're using in the configuration, but basically it's:

* python2.7
* python-yaml


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


How to configure SBC
--------------------

### WiFi connection

Will connect to wifi access points (ex. home, cellphone). I'm using wpa_supplicant because it's easy to configure from shell.

#### Requirements

* wpa_supplicant

#### Setup

1. Install wpasupplicant package
2. Copy and change `configs/sbc/wifi-wpa_supplicant.conf` to `/etc/wpa_supplicant/wpa_supplicant.conf` following the comments inside
3. Change access permissions to the file `/etc/wpa_supplicant/wpa_supplicant.conf` because it contains passwords:
  ```bash
  sudo chmod 600 /etc/wpa_supplicant/wpa_supplicant.conf`
  ```
4. Copy `configs/sbc/network-interfaces.conf` to `/etc/network/interfaces` to make sure it contains only loopback & interfaces.d configs including
5. Copy `configs/sbc/wifi-network-interfaces-wlan0.conf` to `/etc/network/interfaces.d/wlan0.conf`
6. Make sure, that there is no other network managers in the system, like NetworkManager or connmand
7. Restart networking service or reboot

### Ethernet access point

Help with direct connection to the board if wireless is not an option.

#### Requirements

* dnsmasq

#### Setup

1. Install dnsmasq package
2. Check that it's enabled in `/etc/default/dnsmasq`
3. Copy `configs/sbc/network-dnsmasq.conf` to `/etc/dnsmasq.conf` to make sure that there is nothing, but including configs from .d directory
4. Copy `~/Projects/tracker/configs/sbc/ethernet-dnsmasq-dhcp.conf` to `/etc/dnsmasq.d/dhcp.conf` and check comments inside
5. Copy `configs/sbc/network-interfaces.conf` to `/etc/network/interfaces` to make sure it contains only loopback & interfaces.d configs including
6. Copy `configs/sbc/ethernet-network-interfaces-eth0.conf` to `/etc/network/interfaces.d/eth0.conf`
7. Restart networking service or reboot

### Read only root

Will save your sdcard & data on accidental poweroff.

#### Setup

Depends on what the SBC you using
* TODO

### Watchdog

Will reboot SBC on freeze.

#### Setup

Depends on what the SBC you using
* TODO

### Audio

If you gonna use audio features (like aux) it will be great to configure your default alsa output

#### Setup

Depends on what the SBC you using
* TODO

### Display

You need to make sure, that your video output has good resolution to see camera/console output

#### Setup

Depends on what the SBC you using and what the display you using. I bought rear view mirror with 4.3" display that has 2 composite inputs (default and parking camera).

* Tinkerboard Armbian:
  Just need to set framebuffer resolution in kernel additional options and recreate image. After that reboot.
  ```
  $ grep 'extraargs' /boot/armbianEnv.txt
  extraargs=video=HDMI-A-1:720x480@60
  $ sudo mkimage -C none -A arm -T script -d /boot/boot.cmd /boot/boot.scr
  ```
* Raspberry Pi 3:
  Edit /boot/config.txt and change hdmi options and play with overscan if you need. After that reboot.
  ```
  $ grep '^hdmi' /boot/config.txt
  hdmi_force_hotplug=1
  hdmi_group=1
  hdmi_mode=3
  ```


Install Tracker
---------------

Unfortunate, it's hard to standartize this pretty tough process, but I tried to make it simple. Let's begin:

1. Create directory `/srv/tracker` - it will contain sources of the application
2. Install `git` package
3. Clone git repository from GitHub. Tracker will not change a bit in the directory, so it's a good idea to leave it with only ro access for unprivileged users
  ```bash
  sudo git clone https://github.com/rabits/tracker.git /srv/tracker
  ```
4. Now we can run `/srv/tracker/setup.sh` to:
  * Create `tracker` service user and add it to the required groups
  * Allow sudo access to run root-access required applications
  * Register service in systemd and enable it to autostart
  * Install/build required packages
5. Make sure, that you have /dev/gpiomem with right rw access for gpio group
6. Start tracker service and check logs:
  ```bash
  sudo systemctl start tracker
  journald -u tracker
  ```
7. Check for errors and if found something, well, it's time to figure it out :)

Hardware
--------

### SBC - single board computers

Just one SBC for now looks really good - others has their issues that could be solved.

Main issue for all the boards is power management (RTC Sleep, RTC poweron, powered off consumption, waiting power consumption).
I think that RTC sleep is not our choice (it still will consume ~0.5W and I saw just a little number of SBC that could sleep properly) - so RTC poweron will work to wake up every 5-10 minutes, do business and power off again.
Also we need to make sure, that SBC will wake up when someone opens the door and quickly boot to provide services we need. So connection to interior light is necessary to get such signal.

List of features the `tracker` need:
* **Power management** - there is no issues with power when engine is running, but when engine is stopped we using battery and 1-3W could drain your battery dead in a week.
  Tracker will poweroff when is no ignition is present and awake only to check the status for a short period of time.
  `RTC` & `rtcwake` should work well for the purpose, but if not - there should be some timer wich will cut the power and bring it back after some delay.
* **USB Host** - a number of devices could be connected through USB interface (like cameras, hdmi-to-composite, OBD debug port, WiFi & Bluetooth dongles, audio card).
  So powering of the devices through USB could be main issue, so make sure you have good powering abilities (like 12V to 5V 3Amp DC-DC converter).
* **GPIO** - to know about car basic status (ignition on, door open...) you will use it as triggers for events (power on, music start...) and control devices by triggering GPIO outputs.
  It provide useful I2C interface to connect additional sensors (current, voltage, temperature...).
* **Storage** - integrated eMMC or microSD card for 8GB will work well enough.
  Spend some time on research how to make root read only - it will save alot of your time later, when mechanics will disconnect negative clemma from the battery to maintenance.
  If you need to store some logs/videos - more free storage is better.

Optional:
* **WiFi** - network connection to get ssh access and connection to internet to send logs & metrics about your car to personal tracker server. As usual - could be replaced by USB dongle.
* **Bluetooth** - use onboard one or use USB dongle to listen your cellphone music wirelessly.
* **AUX/Jack 3.5 output** - it's always good to have good soundcard onboard or you can use USB sound card. Some filter also could be good idea to lower alternator noise. Could be replaced by HDMI-to-AV adapter.
* **Ethernet** - to connect to your SBC wired from notebook, debugging and so on.
* **HDMI / Composite output** - to see the connected cameras live video & some data from the SBC. Also could help with debugging if you will connect your keyboard.
* **GSM / GPS** - good to have such ability to have internet connection without WiFi and provide GPS coordinates about the car location.

#### ASUS Tinkerboard

Armbian requires additional fixes to get sound via jack & bluetooth working, but overall looks like a better choice now.

##### Issues

* Armbian 5.52.180715 Bionic Next (kernel 4.14.55-rockchip):
  * rtcwake with mem failed on wake
* TinkerOS linaro v2.0.5 (kernel 4.4.71):
  * rtcwake with off not wake up

##### Fixes

* Default alsa analog output:
/etc/asound.conf:
```
pcm.!default {
  type plug
  slave {
    pcm "hw:0,2"
  }
}
ctl.!default {
  type hw
  card 0
}
```

###### Optimizations

* NMI Watchdog turn off: `echo 0 | sudo tee /proc/sys/kernel/nmi_watchdog` ~0mA
* VM Writeback timeout: `echo 1500 | sudo tee /proc/sys/vm/dirty_writeback_centisecs` ~0mA
* Autosuspend for usbaudio: `echo auto | sudo tee /sys/bus/usb/devices/3-1/power/control` ~50mA

##### Power

* Default: 370mA
* Optimized: 320mA
* RTC Sleep: not working
* RTC PowerOn: working
* Powered Off: 0mA
* Bluetooth music playing: ???mA

#### Raspberry PI 3

##### Issues

* No RTC & power management - it will eat your battery even if it's powered off and there is no way to sleep.
* Jittery BT audio due to wifi+bt issue: https://github.com/Arkq/bluez-alsa/issues/60 - it's better to use USB BT adapter
  You could disable the internal bluetooth permanently by adding next `/boot/config.txt` lines and disable the sytemd htcuart service:
  ```
  dtoverlay=pi3-disable-bt
  ```
  ```
  sudo systemctl disable hciuart
  ```
* Poor quality of jack audio output. Could be improved by adding to `/boot/config.txt`:
  ```
  audio_pwm_mode=2
  ```

##### Power

* Default: 230mA
* Powered Off: 100mA (yeah, wut)
* Bluetooth music playing: 240-290mA

###### Optimizations

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

#### Nano PI M3

Tested both armbian & original nanopi images.

##### Issues

* Sleep not supported

##### Power

* Default: 270mA
* RTC Sleep: UNSUPPORTED
* Powered Off: 0mA
* Bluetooth music playing: ???mA

#### Le Potato aml-s905x-cc

Tested on latest armbian 5.42 with kernel 4.16.0

##### Issues

* No WiFi & Bluetooth, but USB adapters working well.
* No built-in RTC so no rtcwake
* No analog audio supported (but hw existing)

##### Power

* Default: 350mA
* RTC Sleep: UNSUPPORTED
* Powered Off: reboot instead
* Bluetooth music playing: ???mA

#### Banana PI M2 Berry

##### Issues

* No initialization after sleep `rtcwake -m mem -s 60`, but power led become active

##### Power

* Default: 170mA
* RTC Sleep: ???mA
* Powered Off: 0mA
* Bluetooth music playing: ???mA


### Components

* Bluetooth (BT Audio receiver)
* WiFi (remote access, configuration, update, send logs)
* HDMI (Display or HUD projector)
* Analog stereo audio output (BT Audio receiver, notifications)
* GPIOx4 (Ignition, Power, Audio enable, GSM module power switch)
* I2C (ADC connection)
* UART (connection with GSM/GPS module)
* GPS (get location)
* GSM Data (2G, 3G, 4G - non-wifi internet access)
* USB Host (ALDL connection)
* RTC (sleep & power save)

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

#### GSM/GPS SIM5320A

It is possible to connect gsm and gps module to track your position and have persistent internet connection.
This one was tested with "DIYMall SIM5320A 3G GSM GPRS GPS Expansion Board WCDMA + HSDPA" - but any GSM module could be adapted.

##### Power

* GSM board enabled: +60mA
* GPS enabled: +30mA

##### Configuration

Additional configuration is required to enable communication channel between rpi & module.
HW UART ttyAMA0 still will be used by bluetooth (and it's good, we need a strong connection) and we can use ttyS0 to interact with our GSM module.

* /boot/config.txt
```
# Enabling mini uart to rule the GSM module
enable_uart=1 # Now UART GPIO pins (GPIO14, GPIO15) will be used by miniUART
core_freq=250 # Required to have constant baud rates
```

#### OBD1 ALDL-USB Cable 1320 Electronics

Check ALDL160 [README](doc/ALDL_160baud/README.md) for more info

#### ADS1115 via I2C

Checking input voltage requires at lease one Analog-Digital Converter.

Simple voltage divider (~1/10) and zener diode used to get appropriate value.

#### HDMI-to-AV "Tendak HDMI to AV CVBS Composite Converter Adapter"

Convert HDMI to composite video output, not using the audio output due to poor sound quality.

#### Rear view mirror with display "Master Tailgaters OEM Rear View Mirror"

I'm using rear view mirror to see what's happening when I'm parking in reverse and it allows me to see the front camera to park safely. Good solution if you don't want to change your head unit.

#### Front view camera "TOTUOKEY Wide Angle Camera"

Connected by USB and has wide angle lens (100 deg in fact) but was modified to increase cable to camera module and putted into 3d-printed case to protect.

##### Issues

* Found that to work correctly all such cameras requires set the uvcvideo quirks to `2`:
  ```
  $ echo 2 | sudo tee /sys/module/uvcvideo/parameters/quirks
  ```
  Or permanently:
  ```
  echo 'options uvcvideo quirks=0x2' | sudo tee /etc/modprobe.d/uvcvideo-camera.conf
  ```


TODO
----

* Framebuffer Display support - showing camera and required data
* TextToSpeech interface & audio notification support - verbal events & status


Support
-------
If you like this project, you can support our open-source development by a small Bitcoin donation.

Bitcoin wallet: `15phQNwkVs3fXxvxzBkhuhXA2xoKikPfUy`

