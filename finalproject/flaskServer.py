#!/usr/bin/python

#imports flask, json, and sql for script use
from flask import Flask, render_template, jsonify, Response
import sqlite3 as sql
import json

app = Flask(__name__)

#implements index.html code
@app.route("/")
def index():
	return render_template('index.html')

#grabs temperature data from weather.db for temperature gauge and temperature graph
@app.route("/sqlData1")
def chartData1():
	con1 = sql.connect('../../EL2020/finalproject/weather.db')
	cur1 = con1.cursor()
	con1.row_factory = sql.Row
	cur1.execute("SELECT Date, Temperature FROM weather WHERE Temperature > 40")
	dataset1 = cur1.fetchall()
	print (dataset1)
	chartData1 = []
	for row in dataset1:
		chartData1.append({"Date": row[0],"Temperature": float(row[1])})
	return Response(json.dumps(chartData1), mimetype='application/json')

#grabs humidity data from weather.db for humidity gauge and humidity graph
@app.route("/sqlData2")
def chartData2():
	con2 = sql.connect('../../EL2020/finalproject/weather.db')
	cur2 = con2.cursor()
	con2.row_factory = sql.Row
	cur2.execute("SELECT Date, Humidity FROM weather WHERE Humidity < 100")
	dataset2 = cur2.fetchall()
	print (dataset2)
	chartData2 = []
	for row in dataset2:
		chartData2.append({"Date": row[0],"Humidity": float(row[1])})
	return Response(json.dumps(chartData2), mimetype='application/json')

#grabs air pressure at both sea level and current altitude data for pressure graph and pressure gauges
@app.route("/sqlData3")
def chartData3():
	con3 = sql.connect('../../EL2020/finalproject/weather.db')
	cur3 = con3.cursor()
	con3.row_factory = sql.Row
	cur3.execute("SELECT Date, Pressure, SeaPressure FROM weather")
	dataset3 = cur3.fetchall()
	print(dataset3)
	chartData3 = []
	for row in dataset3:
		chartData3.append({"Date": row[0],"Pressure": float(row[1]),"SeaPressure": float(row[2])})
	return Response(json.dumps(chartData3), mimetype='application/json')

#grabs altitude data for current altitude output
@app.route("/sqlData4")
def Alt():
	con4 = sql.connect('../../EL2020/finalproject/weather.db')
	cur4 = con4.cursor()
	con4.row_factory = sql.Row
	cur4.execute("SELECT Altitude FROM weather")
	dataset4 = cur4.fetchall()
	print(dataset4)
	chartData4 = []
	for row in dataset4:
		chartData4.append({"Altitude": float(row[0])})
	return Response(json.dumps(chartData4), mimetype='application/json')

#grabs raining or not raining data for output
@app.route("/sqlData5")
def ROS():
	con5 = sql.connect('../../EL2020/finalproject/weather.db')
	cur5 = con5.cursor()
	con5.row_factory = sql.Row
	cur5.execute("SELECT RainOrShine FROM weather")
	dataset5 = cur5.fetchall()
	print(dataset5)
	chartData5 = []
	for row in dataset5:
		chartData5.append({"RainOrShine": row[0]})
	return Response(json.dumps(chartData5), mimetype='application/json')

#grabs day or night data for output
@app.route("/sqlData6")
def DON():
	con6 = sql.connect('../../EL2020/finalproject/weather.db')
	cur6 = con6.cursor()
	con6.row_factory = sql.Row
	cur6.execute("SELECT DayOrNight FROM weather")
	dataset6 = cur6.fetchall()
	print(dataset6)
	chartData6 = []
	for row in dataset6:
		chartData6.append({"DayOrNight": row[0]})
	return Response(json.dumps(chartData6), mimetype='application/json')

#grabs temperature and humidity data for temperature vs humidity scatter plot
@app.route("/sqlData7")
def chartData7():
	con7 = sql.connect('../../EL2020/finalproject/weather.db')
	cur7 = con7.cursor()
	con7.row_factory = sql.Row
	cur7.execute("SELECT Temperature, Humidity FROM weather WHERE (Temperature > 40) AND (Humidity < 100)")
	dataset7 = cur7.fetchall()
	print(dataset7)
	chartData7 = []
	for row in dataset7:
		chartData7.append({"Temperature": float(row[0]),"Humidity": float(row[1])})
	return Response(json.dumps(chartData7), mimetype='application/json')

#creates flask server
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=2020, debug=True, use_reloader=False)
