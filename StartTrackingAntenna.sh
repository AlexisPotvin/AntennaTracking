#!/bin/bash

sudo pkill python
sudo killall gpsd
sudo gpsd /dev/ttyAMA0 -F /var/run/gpsd.sock

sudo python TrackingAntenna.py
