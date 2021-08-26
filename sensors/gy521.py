#!/usr/bin/env python
import smbus
import sys
if len(sys.argv)!=2:
  raise OSError('Invalid number of arguments')
bus=smbus.SMBus(1)
bus.write_byte_data(0x68,0x6b,0)
def read(reg):
  val=(bus.read_byte_data(0x68,reg)<<8)+bus.read_byte_data(0x68,reg+1)
  if val>=0x8000:
    return val-0x10000
  else:
    return val
with open(sys.argv[1],'wt') as f:
  f.write('{"gx":'+read(0x43)/0x83+',"gy":'+read(0x45)/0x83+',"gz":'+read(0x47)/0x83+',"ax":'+read(0x3b)/0x8000+',"ay":'+read(0x3d)/0x8000+',"az":'+read(0x3f)/0x8000+'}')

