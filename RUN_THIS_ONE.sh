#!/bin/sh

# Install desktop file
sudo cp -pvr photo-frame-gtk-autostart.desktop /etc/xdg/autostart/;
sudo chown root:root /etc/xdg/autostart/photo-frame-gtk-autostart.desktop;
sudo reboot;


# DISPLAY=:0 nohup python3 photoframegtk.py