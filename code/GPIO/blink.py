import RPi.GPIO as GPIO
import time
import signal
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(26, GPIO.IN)

def blinkOnce(pin):
	GPIO.output(pin,True)
	time.sleep(1)
	GPIO.output(pin,False)
	time.sleep(1)
try:
	while True:
		input_state = GPIO.input(26)
		if input_state == True:
			blinkOnce(17)

except KeyboardInterrupt:
	print('Yeh see ya layta mate!')
	GPIO.cleanup()
