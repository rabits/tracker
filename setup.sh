sudo useradd tracker
sudo usermod -aG audio,dialout,bluetooth,netdev,gpio,i2c tracker

# Sudo access for tracker user to run root operations
echo "tracker ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/50-tracker

# Installing required packets as module dependencies:
# - Core: python-yaml
# - GPIO: python-rpi.gpio
# - Bluetooth: bluez bluealsa python-dbus
# - ALDL160: python-serial
# - GSMGPS: python-serial ppp
# - WiFi: hostapd dnsmasq
# - ADS1115: python-smbus
sudo apt install \
    python-yaml \
    python-rpi.gpio \
    bluez \
    bluealsa \
    python-dbus \
    python-serial \
    ppp \
    hostapd \
    dnsmasq \
    python-smbus

# Disable services to manage it manually thru Tracker
sudo service hostapd stop
sudo service dnsmasq stop
sudo systemctl disable hostapd
sudo systemctl disable dnsmasq

# Switching pwm mode to fix the internal analog audio output
echo "audio_pwm_mode=2" | sudo tee -a /boot/config.txt
