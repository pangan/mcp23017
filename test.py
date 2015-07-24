from mcplib import MCP23017

_A = 0
_B = 1
chip = MCP23017()

#chip.cleanup()

chip.set(_A,1,True)
chip.set(_A,0,True)
chip.set(_A,1,False)
chip.set(_A,7,True)

print "p#\tA\tB"
for i in range (0,8):
	print "%s\t%s\t%s" %(i, chip.get(_A,i), chip.get(_B,i))