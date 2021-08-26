#!/usr/bin/env python
import smbus
import sys
import time
if len(sys.argv)!=2:
  raise OSError('Invalid number of arguments')
bus=smbus.SMBus(1)
bus.write_byte_data(0x68,0x6b,0)
def read(reg):
  time.sleep(0.2)
  val=(bus.read_byte_data(0x68,reg)<<8)+bus.read_byte_data(0x68,reg+1)
  if val>=0x8000:
    return val-0x10000
  else:
    return val
with open(sys.argv[1],'wt') as f:
  f.write('{"gx":'+str(read(0x43))+',"gy":'+str(read(0x45))+',"gz":'+str(read(0x47))+',"ax":'+str(read(0x3b))+',"ay":'+str(read(0x3d))+',"az":'+str(read(0x3f))+'}')

