#!/bin/sh

sudo apt update;
sudo apt dist-upgrade;
sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-4.0 -y;


CWD="/home/pipi/photo_frame_gtk/"
SERVICE_DIR="/etc/systemd/system/"
SERVICE_FILE="/home/pipi/photo_frame_gtk/photoframegtk.service"
BIN_DIR="/usr/bin/"
BIN_FILE="/usr/bin/photoframegtk.py"
SRC_FILE="/home/pipi/photo_frame_gtk/photoframegtk.py"

cd $CWD;
sudo mv $SERVICE_FILE $SERVICE_DIR;
sudo mv $SRC_FILE $BIN_FILE;
sudo chmod +rx $BIN_FILE;
sudo chown root:root $BIN_FILE;
sudo systemctl daemon-reload;
sudo systemctl enable photoframegtk.service;
sudo systemctl start photoframegtk.service;
sudo systemctl status photoframegtk.service;

