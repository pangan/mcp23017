from mcplib import MCP23017

chip = MCP23017()

#chip.cleanup()

chip.set(1,True)
print "---"
chip.set(0,True)
chip.set(1,False)
chip.set(7,True)

for i in range (0,8):
	print "%s:%s" %(i, chip.get(i))