from mcplib import MCP23017
import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGGER = 23
GPIO_ECHO = 24


GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER, False)

time.sleep(.5)


_A = 0
_B = 1
chip = MCP23017()

#chip.cleanup()
#GPIO.output(GPIO_TRIGGER, True)

#chip.set(_B,0,False)
#time.sleep(0.00001)

#chip.set(_B,0,1)
#time.sleep(0.001)
#chip.set(_B,0,0)

#GPIO.output(GPIO_TRIGGER, False)
'''
try:
	while True:
		h = chip.get(_A)
		if h>0: print h

	
except KeyboardInterrupt:
	GPIO.cleanup()
	chip.close()
	exit
	
'''
'''
while chip.get(_B) == 0:
	print "sss"
	start = time.time()


while chip.get(_B) != 0:
	stop = time.time()
	print chip.get(_B)


print "fff"
'''


'''
try:
	while True:
		print chip.get(_B)
except KeyboardInterrupt:
	chip.close()
	exit
'''	
'''

'''

# Use BCM GPIO references
# instead of physical pin numbers

print "Ultrasonic Measurement"

# Set pins as output and input

# Allow module to settle
time.sleep(0.5)

while True:

	# Send 10us pulse to trigger
	GPIO.output(GPIO_TRIGGER, True)
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, False)
	#chip.set(_B,0,True)
	#time.sleep(0.00001)
	#chip.set(_B,0,False)



	start = time.time()

	#while chip.get(_B)==0:
	#  start = time.time()
	#print "ffff"
	sen = 0 
	while sen ==0:
	  start = time.time()
	  #sen = GPIO.input(GPIO_ECHO)
	  sen = chip.get(_B)
	print "--->"
	while sen ==1:
	  stop = time.time()
	  #sen = GPIO.input(GPIO_ECHO)
	  sen = chip.get(_B)


	# Calculate pulse length
	elapsed = stop-start

	# Distance pulse travelled in that time is time
	# multiplied by the speed of sound (cm/s)
	distance = elapsed * 34000

	# That was the distance there and back so halve the value
	distance = distance / 2

	print "Distance : %.1f" % distance
	time.sleep(1)

# Reset GPIO settings
GPIO.cleanup()
