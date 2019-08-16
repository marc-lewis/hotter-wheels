#!/bin/sh

# deps for approvxeng.input (approxeng.github.io/approxeng.input/bluetooth.html)
sudo apt-get install python-dev python-pip gcc
pip3 install approxeng.input

# enable constant pairing with bluetooth controller
# see approxeng.github.io/approxeng.input/bluetooth.html
echo "options bluetooth disable_ertm=Y" | sudo tee -a /etc/modprobe.d/bluetooth.conf

# bluetoothctl 
# press pairing button on controller
# pair C8:3F:26:36:53:63
# press pairing button on controller
# connect C8:3F:26:36:53:63
# trust C8:3F:26:36:53:63
