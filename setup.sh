sudo useradd tracker
sudo usermod -aG audio,dialout,bluetooth tracker

# Sudo access for tracker user to run root operations
echo "tracker ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/50-onebutton

sudo apt install bluez bluealsa python-bluez python-yaml python-dbus

# Switching pwm mode to fix audio
echo "audio_pwm_mode=2" | sudo tee -a /boot/config.txt
