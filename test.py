from mcplib import MCP23017

_A = 0
_B = 1
chip = MCP23017()

#chip.cleanup()

chip.set(_A,1,True)
chip.set(_A,0,True)
chip.set(_A,1,False)
chip.set(_A,6,True)

print "p#\tvalue"

for i in range (0,2):
	print "%s\t%s" %(i,bin(chip.get(i)))

try:
	while 1:
		pass
except KeyboardInterrupt:
	chip.close()
	exit
	