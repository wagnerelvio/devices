#!/usr/bin/env python
# -*- coding: ISO8859-1 -*-
# -*- coding: UTF-8 -*-
import spidev
import cgi
#import glob
import time
import os


from datetime import datetime

today = datetime.now()
day = today.day
month = today.month
year = today.year

#print "Data: ", time.strftime('%d %b %Y'),time.strftime ('%H:%M:%S'),  "|"

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

temp_sensor = '/sys/bus/w1/devices/28-0000067beb98/w1_slave'
def temp_raw():
	f = open(temp_sensor, 'r')
	lines = f.readlines()
	f.close()
	return lines

def read_temp():
	lines = temp_raw()
	while lines[0].strip()[-3:] != 'YES':
		time.sleep(5)
		lines = temp_raw()
	temp_output = lines[1].find('t=')
	if temp_output != -1:
		temp_string = lines[1].strip()[temp_output+2:]
		temp_c = float(temp_string) / 1000.0
		temp_f = temp_c * 9.0 / 5.0 + 32.0
		return temp_c, temp_f

while True:
      #  print("Valores:", read_temp())
#	print("Ola")
	time.sleep(1)
        print ("Data: ", time.strftime('%d %b %Y'),time.strftime ('%H:%M:%S'),  "|" , read_temp())
##############################

