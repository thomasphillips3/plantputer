#!/usr/bin/python

import sys
import time
import Adafruit_DHT
from gpiozero import DigitalInputDevice
import xlwt
from xlwt import Workbook

d0_input = DigitalInputDevice(17)
wb = Workbook()
data_sheet = wb.add_sheet('data')
row = 1
col = 1

while True:
    humidity, temperature = Adafruit_DHT.read_retry(11,4)
    print('Temp: {0:0.1f} C Humidity: {1:0.1f} %'.format(temperature, humidity))
    data_sheet.write(row, col, humidity)
    col+=1
    data_sheet.write(row, col, temperature)
    row+=1
    data_sheet.write(row, col, d0_input.value)

    if (not d0_input.value):
        print('wet')
    else:
        print('dry')
        #time.sleep(2)
    row+=1
    col = 1
    wb.save('plantputerdata.xls')
