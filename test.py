from mcplib import MCP23017
import time

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
		0b00000011,
		0b00000010,
		0b00000110,
		0b00000100,
		0b00001100,
		0b00001000,
		0b00001001]


print "p#\tvalue"

a=0
direct = 1
try:
	while 1:
		#chip.set(_A,0,seq[a][0])
		#chip.set(_A,1,seq[a][1])
		#chip.set(_A,2,seq[a][2])
		#chip.set(_A,3,seq[a][3])
		chip.set_paral(_A,seqb[a])
		a = a + direct
		if a==8: 
			a=0
		if a==-1:
			a=7
		time.sleep(0.001)
		
except KeyboardInterrupt:
	chip.close()
	exit
	