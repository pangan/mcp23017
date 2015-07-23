class MCP23017(object):

	def __init__(self):
		self.ports = [0,0,0,0,0,0,0,0]
		

	def p2add(self, port):
		return pow(2, port)

	def cleanup(self):
		self.ports = [0,0,0,0,0,0,0,0]
		# send 0 to port

	def set(self, port, value):
		# set hardware p2add(port) = value
		self.ports[port] = value
		port_val = 0
		inx = 0
		for i in self.ports:
			port_val += i and pow (2,inx)
			inx += 1 

		print " %s to hardware " %port_val



	def get(self, port):
		# read port p2add(port)
		return self.ports[port] 




		