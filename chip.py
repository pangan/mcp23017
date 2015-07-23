import smbus
import time,sys
 
def ioa(dec_port):

	return pow(2,dec_port)



#bus = smbus.SMBus(0)  # Rev 1 Pi uses 0
bus = smbus.SMBus(1) # Rev 2 Pi uses 1
 
DEVICE = 0x20 # Device address (A0-A2)
IODIRA = 0x00 # Pin direction register
OLATA  = 0x14 # Register for outputs
GPIOA  = 0x12 # Register for inputs

IODIRB = 0x01 # Pin direction register
OLATB  = 0x15 # Register for outputs
GPIOB  = 0x13 # Register for inputs

# Set all GPA pins as outputs by setting
# all bits of IODIRA register to 0
bus.write_byte_data(DEVICE,IODIRA,0x00)
bus.write_byte_data(DEVICE,IODIRB,0x00) 
# Set output all 7 output bits to 0
bus.write_byte_data(DEVICE,OLATA,0)
bus.write_byte_data(DEVICE,OLATB,0)
 



try:
	while 1:
		for MyData in range(0,8):
		  # Count from 1 to 8 which in binary will count
		  # from 001 to 111
		  bus.write_byte_data(DEVICE,OLATA,ioa(MyData))
		  bus.write_byte_data(DEVICE,OLATB,ioa(MyData))
		  time.sleep(.1)
except KeyboardInterrupt:
	bus.write_byte_data(DEVICE,OLATA,0)
	bus.write_byte_data(DEVICE,OLATB,0)
	exit



''' 
# Set all bits to zero

bus.write_byte_data(DEVICE,OLATA,ioa(0))
time.sleep(3)
'''
