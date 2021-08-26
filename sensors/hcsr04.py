#!/usr/bin/env python
import RPi.GPIO as gpio
import time
import sys
if len(sys.argv)!=2:
  raise OSError('Invalid number of arguments')
gpio.setmode(gpio.BCM)
GPIO_TRIGGER,GPIO_ECHO=18,24
gpio.setup(GPIO_TRIGGER,gpio.OUT)
gpio.setup(GPIO_ECHO,gpio.IN)
def dist():
  gpio.output(GPIO_TRIGGER,True)
  time.sleep(0.00001)
  gpio.output(GPIO_TRIGGER,False)
  stime,etime=time.time(),time.time()
  while gpio.input(GPIO_ECHO)==0:
    stime=time.time()
  while gpio.input(GPIO_ECHO)==1:
    etime=time.time()
  return (etime-stime)*34300/2
with open(sys.argv[1],'wt') as f:
  f.write(dist())
gpio.cleanup()

