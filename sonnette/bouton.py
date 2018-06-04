#!/usr/bin/env python3.5
#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(12)
    if input_state == False:
        print('Button Pressed')
        os.popen('aplay sncf.wav')
        time.sleep(0.2)
        os.system('echo "Quelqu un a sonné\n Va voir qui c\'est : http://192.168.137.131:5000/" | mail -s "Bouton pressé" leoliam100@gmail.com')
