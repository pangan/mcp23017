import smbus
class MCP23017(object):

	def __init__(self):
		
		#bus = smbus.SMBus(0)  # Rev 1 Pi uses 0
		self.bus = smbus.SMBus(1) # Rev 2 Pi uses 1
		self.DEVICE = 0x20 # Device address (A0-A2)
		self.IODIRA = 0x00 # Pin direction register
		self.OLATA  = 0x14 # Register for outputs
		self.GPIOA  = 0x12 # Register for inputs

		self.IODIRB = 0x01 # Pin direction register
		self.OLATB  = 0x15 # Register for outputs
		self.GPIOB  = 0x13 # Register for inputs

		# Set all GPA pins as outputs by setting
		# all bits of IODIRA register to 0
		self.bus.write_byte_data(self.DEVICE,self.IODIRA,0x00)
		self.bus.write_byte_data(self.DEVICE,self.IODIRB,0x00) 
		
		self.cleanup()

	def p2add(self, port):
		return pow(2, port)

	def cleanup(self):
		self.ports = [0, 0]
		# Set output all 7 output bits to 0
		self.bus.write_byte_data(self.DEVICE,self.OLATA,0)
		self.bus.write_byte_data(self.DEVICE,self.OLATB,0)

		

	def set(self, bank, port, value):
		if value:
			self.ports[bank] = self.ports[bank] | self.p2add(port)
		else:
			self.ports[bank] = self.ports[bank] & ~ self.p2add(port)

		print " write bank %s , val: %s to hardware "%(bank, self.ports[bank])
		
		# set hardware = self.ports

	def get(self, bank, port):
		# read port p2add(port)
		return bool(self.ports[bank] & self.p2add(port))




		