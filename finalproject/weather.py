import RPi.GPIO as GPIO
import time, datetime, sys, os
import Adafruit_DHT
import Adafruit_BMP.BMP085 as BMP085
import sqlite3 as sql
import smtplib

#connect to weather.db
con = sql.connect('../../EL2020/finalproject/weather.db')
cur = con.cursor()

#Configure Light/Water Sensors
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN)
GPIO.setup(22,GPIO.IN)

#Configure Temperature/Humidity Sensor
pin = 17
sensor = Adafruit_DHT.DHT11

#Configure Barometric Pressure Sensor
pressure_sensor = BMP085.BMP085()

print 'Starting up Weather Station'

#Continuously get values
while True:
	try:

		#Read values from the tempeerature/humidity sensor if we can
		humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

		#Make temperature display in Farenheit
		temperature = temperature * 9/5.0 +32

		#Meters to feet conversion
		altitude = pressure_sensor.read_altitude()
		altitude = altitude / 0.3048

		#Read data from pressure sensor
		press = pressure_sensor.read_pressure()
		press = press / 100.0
		pressure = pressure_sensor.read_sealevel_pressure()
		pressure = pressure / 100.0 #1 mbar = 100 Pa.

		#print if its raining or not
		print('Water Sensor Data Readout:')
		for x in range(0,1):
			water = GPIO.input(22)
			if water == 1:
				RoS = 'It is raining'
				print RoS
			else:
				RoS = 'It is not raining'
				print RoS
		#print if its day or night
		print('Light Sensor Data Readout:')
		input_state = GPIO.input(18)
		if input_state == True:
			DoN = 'It is Nighttime'
			print(DoN)
		else:
			DoN = 'It is Daytime'
			print(DoN)
		#print pressure/altitude
		print('Barometric Pressure Sensor Data Readout:')
		print('Pressure = {0:0.2f} mb'.format(press))
		print('Altitude = {0:0.2f} ft'.format(altitude))
		print('Sealevel Pressure = {0:0.2f} mb'.format(pressure))
		#print temperature/humidity
		print('Temperature and Humidity Sensor Data Readout:')
		print('Temperature={0:0.1f}*F, Humidity={1:0.1f}%'.format(temperature, humidity))
		#log data all data into database file weather.db
		cur.execute('INSERT INTO weather values(?,?,?,?,?,?,?,?)', (time.strftime('%Y-%m-%d %H:%M:%S'),str(RoS),str(DoN),float(temperature),float(humidity),float(press),float(altitude),float(pressure)))
		con.commit()
		time.sleep(300)
		print('--------------------------------')
		continue

	except KeyboardInterrupt:
		GPIO.cleanup()
		break
