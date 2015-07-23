class MCP23017(object):

	def __init__(self):
		self.ports = 0

	def p2add(self, port):
		return pow(2, port)

	def cleanup(self):
		self.ports = 0
		# send 0 to port

	def set(self, port, value):
		if value:
			self.ports = self.ports | self.p2add(port)
		else:
			self.ports = self.ports & ~ self.p2add(port)

		print " %s to hardware "%self.ports
		# set hardware = self.ports

	def get(self, port):
		# read port p2add(port)
		return bool(self.ports & self.p2add(port))




		