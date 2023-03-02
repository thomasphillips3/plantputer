#!/usr/bin/python

import sys
import time
import Adafruit_DHT
from gpiozero import DigitalInputDevice
import xlwt
from xlwt import Workbook
import sqlite3

d0_input = DigitalInputDevice(17)
wb = Workbook()
data_sheet = wb.add_sheet('data')
row = 1
col = 1

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def write_to_database(value):
    conn = sqlite3.connect('plantputer.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS plantputer(temp TEXT, humidity TEXT)''')
    c.execute("INSERT INTO plantputer VALUES('','')")

while True:
    humidity, temperature = Adafruit_DHT.read_retry(11,4)
    fahrenheit = celsius_to_fahrenheit(temperature)
    print('Temp: {0:0.1f} F Humidity: {1:0.1f} %'.format(fahrenheit, humidity))
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
