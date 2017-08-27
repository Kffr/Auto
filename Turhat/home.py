#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(26)
    if input_state == False:
        os.system('sudo pkill -f obd_gui.py')
	os.system('sudo pkill -f gui.py')
	os.system('sudo python /home/pi/pyobd-pi/gui.py &')
        time.sleep(0.01)
