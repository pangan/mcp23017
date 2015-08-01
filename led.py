from mcplib import MCP23017
import time
import random

_A = 0
_B = 1
chip = MCP23017()

#chip.cleanup()

seq=[[1,0,0,0],
	[1,1,0,0],
	[0,1,0,0],
	[0,1,1,0],
	[0,0,1,0],
	[0,0,1,1],
	[0,0,0,1],
	[1,0,0,1]]

seqb = [0b00000001,
		0b00000010,
		0b00000100,
		0b00001000,
		0b00010000,
		0b00100000,
		0b01000000,
		0b10000000]


print "p#\tvalue"

a=0
direct = -1
try:
	while 1:
		#chip.set(_A,0,seq[a][0])
		#chip.set(_A,1,seq[a][1])
		#chip.set(_A,2,seq[a][2])
		#chip.set(_A,3,seq[a][3])
		chip.set_paral(_A,seqb[a])
		direct = random.choice([-1,1])
		a = a + direct
		if a==8: 
			a=0
		if a==-1:
			a=7
		time.sleep(.2)
		
except KeyboardInterrupt:
	chip.close()
	exit
	