import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import os

redPin = 27
tempPin = 17
buttonPin = 26

tempSensor = Adafruit_DHT.DHT11

blinkDur = .1
blinkTime = 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN)

def oneBlink(pin):
	GPIO.output(pin,True)
	time.sleep(blinkDur)
	GPIO.output(pin,False)
	time.sleep(blinkDur)

def readF(tempPin):
	humidity, temperature = Adafruit_DHT.read_retry(tempSensor, tempPin)
	temperature = temperature * 9/5.0 +32
	if humidity is not None and temperature is not None:
		tempFahr = '{0:0.1f}*F'.format(temperature)
		hum = '{0:0.1f}%'.format(humidity)
	else:
		print('Error Reading Sensor')

	return tempFahr,hum

try:
	with open("../../log/tempLog.db" , "a") as log:

		while True:
			input_state = GPIO.input(buttonPin)
			if input_state == True:
				for i in range (blinkTime):
					oneBlink(redPin)
				time.sleep(.2)
				while True:
					data = readF(tempPin)
					print (data)
					log.write("{0},{1}\n" .format(time.strftime("%Y-%m-%d %H:%M:%S"),str(data)))
					time.sleep(60)

except KeyboardInterrupt:
	print('Thanks for Blinking and Thinking!')
	GPIO.cleanup()

