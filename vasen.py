#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import pyautogui
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
	time.sleep(0.1)
	input_state1 = GPIO.input(24)
	input_state2 = GPIO.input(23)
	input_state3 = GPIO.input(17)
	input_state4 = GPIO.input(26)
	if input_state1 == False:
		pyautogui.press('left')
		
	elif input_state2 == False:
		pyautogui.press('right')
		
	elif input_state3 == False:
		pyautogui.press('enter')
		
	elif input_state4 == False:
		os.system('sudo pkill -f obd_gui.py')
		os.system('sudo pkill -f gui.py')
		os.system('sudo python /home/pi/pyobd-pi/gui.py &')
		
