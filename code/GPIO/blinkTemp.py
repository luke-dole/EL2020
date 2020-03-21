import RPi.GPIO as GPIO
import Adafruit_DHT as DHT
import time
import os
import sqlite3 as sql
import smtplib

redPin = 27
greenPin = 22
tempPin = 17

tempSensor = DHT.DHT11

blinkDur = .1
blinkTime = 7

con = sql.connect('../../log/tempLog.db')
cur = con.cursor()

GPIO.setmode(GPIO.BCM)
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)

def oneBlink(pin):
	GPIO.output(pin,True)
	time.sleep(blinkDur)
	GPIO.output(pin,False)
	time.sleep(blinkDur)


def readF(tempPin):
	humidity, temperature = DHT.read_retry(tempSensor, tempPin)
	temperature = temperature * 9/5.0 +32
	if humidity is not None and temperature is not None:
		tempFahr = '{0:0.1f}'.format(temperature)
		hum = '{1:0.1f}'.format(temperature, humidity)
	else:
		print('Error Reading Sensor')

	return tempFahr, hum

oldTime = 60

tempFahr, hum = readF(tempPin)

try:
	while True:
		if 68 <= float(tempFahr) <= 78:
			eChk = 0
			GPIO.output(redPin,False)
			GPIO.output(greenPin,True)
		else:
			GPIO.output(greenPin,False)
			oneBlink(redPin)

		if time.time() - oldTime > 59:
			tempFahr, hum = readF(tempPin)
			cur.execute('INSERT INTO tempLog values(?,?,?)', (time.strftime('%Y-%m-%d %H:%M:%S'),tempFahr,hum))
			con.commit()
			table = con.execute("select * from tempLog")
			os.system('clear')
			print "%-30s %-20s %-20s" %("Date/Time", "Temp", "Humidity")
			for row in table:
				print "%-30s %-20s %-20s" %(row[0], row[1], row[2])
			oldTime = time.time()

except KeyboardInterrupt:
	print('Thanks for Blinking and Thinking!')
	GPIO.cleanup()

