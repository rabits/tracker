#!/bin/sh -e

sudo useradd tracker
sudo usermod -aG audio,video,dialout,bluetooth,netdev,gpio,i2c tracker

# Sudo access for tracker user to run root operations
echo "tracker ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/50-tracker

# Installing required packets as module dependencies:
# - Core: python-yaml
# - Bluetooth: bluez bluealsa python-dbus python-gobject
# - ALDL160: python-serial
# - GSMGPS: python-serial
# - ADS1115: python-smbus
sudo apt install -y \
    python-yaml \
    bluez \
    python-dbus \
    python-gobject \
    python-serial \
    python-smbus

# Raspbian: Raspberry Pi
if [ -f /etc/rpi-issue ] ; then
    # We have required packages as apt - so just install it
    sudo apt install -y \
        bluealsa \
        python-rpi.gpio
fi

# Armbian: Tinkerboard
if [ -f /etc/armbian.txt ] ; then
    # ----- bluealsa -----
    deps="libasound2-dev libbluetooth-dev libbsd-dev libfdk-aac-dev libglib2.0-dev libncurses5-dev libreadline-dev libsbc-dev libtool"
    # Dependencies to build bluealsa
    sudo apt install -y $(echo "$deps")

    # Getting sources & run build
    git clone https://github.com/Arkq/bluez-alsa /tmp/bluealsa
    cd /tmp/bluealsa
    autoreconf --install && mkdir build && cd build
    ../configure --enable-aac --prefix=/usr/local && make && sudo make install
    cd /tmp
    # Registering & enabling service
    sudo ln -s /srv/tracker/configs/bluealsa.service /etc/systemd/system/bluealsa.service
    sudo systemctl enable bluealsa
    sudo systemctl start bluealsa

    # Cleaning sources & dependencies
    sudo rm -rf /tmp/bluealsa
    sudo apt autoremove --purge -y $(echo "$deps")

    # ----- GPIO -----
    deps="python-dev python2.7-dev"
    # Dependencies to build GPIO
    sudo apt install -y $(echo "$deps")

    # Getting sources & run build
    git clone https://github.com/TinkerBoard/gpio_lib_python /tmp/tinkerboard-gpio
    cd /tmp/tinkerboard-gpio
    sudo python ./setup.py install
    cd /tmp

    # Cleaning sources & dependencies
    sudo rm -rf /tmp/tinkerboard-gpio
    sudo apt autoremove --purge -y $(echo "$deps")
fi

# Registering & enabling service
sudo ln -s /srv/tracker/configs/tracker.service /etc/systemd/system/tracker.service
sudo systemctl enable tracker
