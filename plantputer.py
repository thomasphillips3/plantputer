#!/usr/bin/python

import sys
import time
import Adafruit_DHT
from gpiozero import DigitalInputDevice

d0_input = DigitalInputDevice(17)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(11,4)
    print('Temp: {0:0.1f} C Humidity: {1:0.1f} %'.format(temperature, humidity))

    if (not d0_input.value):
        print('wet')
    else:
        print('dry')
        #time.sleep(2)
