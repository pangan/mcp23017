
class MCP23017(object):

	def __init__(self):
		self.ports = [0,0]
		
	def p2add(self, port):
		return pow(2, port)

	def cleanup(self):
		self.ports = [0, 0]
		# send 0 to port

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




		