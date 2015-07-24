class smbus():
	def __init__(self):
		pass

class SMBus():
	def __init__(self,i):
		self.port={}

	def write_byte_data(self, DEVICE,OLATx,value):
		self.port[OLATx]=value

	def read_byte_data(self, DEVICE, OLATx):
		return self.port[OLATx]



