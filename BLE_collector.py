
import sqlite3
import time
import os
import subprocess
import json
import paho.mqtt.client as mqtt #import the mqtt Client

subprocess.Popen(["/home/pi/bin/BLE-Dongle/start_dongle"]) #start dongle console sdk app
time.sleep(15) # wait 15 seconds for console Dongle Console app to load
broker_address="localhost"

# The callback for when a client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	print ("Connected with result code "+str (rc))
	client.subscribe("dataTX") #subscribe the data strean topic upon connected

# The callback for when a Published message is received from the server
def on_message(client, userdata, msg):
	selectTagToPub(json.loads(msg.payload)["tagType"],client,msg.payload)

def is_EnvironmentSensor(client,msg):
	print (msg)
	timestampUTC = str(json.loads(msg)["timestampUTC"])
	router_mac =str(json.loads(msg)["router_mac"])
	router_lat=float(json.loads(msg)["router_lat"])
	router_long=float(json.loads(msg)["router_long"])
	rssi=int(json.loads(msg)["rssi"])
	Temperature =int(json.loads(msg)["Temperature"])
	Humidity =int(json.loads(msg)["Humidity"])
	Lux = float(json.loads(msg)["VisibleLightPower"])
	uvPower = float(json.loads(msg)["uvPower"])
	pressure=float(json.loads(msg)["Pressure"])
	deviceAddr=str(json.loads(msg)["deviceAddr"])
	MrapFrameCount= int(json.loads(msg)["MrapFrameCount"])
	router_deviceCount=int(json.loads(msg)["router_deviceCount"])
	router_major=int(json.loads(msg)["router_major"])
	router_minor=int(json.loads(msg)["router_minor"])
	
	conn = sqlite3.connect('bleSensor.db') #create a connection to database
	c = conn.cursor()
	c.execute("CREATE TABLE IF NOT EXISTS  environmentSensor (timestampUTC str, routerMac str,routerLat float,routerLong float,rssi int, temperature int,humidity int,"
	"lux float,uvPower float,pressure float, deviceAddress str, MRAPFrameCount int, routerDeviceCount int, routerMajor int, routerMinor int)") #create table if does not exists
	try:
		c.execute("INSERT INTO environmentSensor (timestampUTC,routerMac,routerLat,routerLong,rssi,temperature,humidity,lux,uvPower,pressure,deviceAddress,"
		"MRAPFrameCount,routerDeviceCount,routerMajor,routerMinor) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(timestampUTC, router_mac,router_lat,router_long,rssi,
		Temperature,Humidity,Lux,uvPower,pressure,deviceAddr,MrapFrameCount,router_deviceCount,router_major,router_minor)) #Insert a row of data
	except Error as e:
		print (e)
	conn.commit() #save the changes
	conn.close() #close the connection to the db
	#client.publish("EnvironmentSensor/Temperature",Temperature)
	#client.publish("EnvironmentSensor/Humidity",Humidity)
	#client.publish("EnvironmentSensor/VisibleLightPower",Lux)
	#print ("Published Enviornment Temperature Data:"+ Temperature)

def is_SmartMoistureProbe(client, msg):
	print (msg)
	timestampUTC = str(json.loads(msg)["timestampUTC"])
	router_mac = str(json.loads(msg)["router_mac"])
	dev_type = int(json.loads(msg)["dev_type"])
	router_tl = str(json.loads(msg)["router_tl"])
	router_tlid = str(json.loads(msg)["router_tlid"])
	router_lat= float(json.loads(msg)["router_lat"])
	router_long= float(json.loads(msg)["router_long"])
	nodeAddr = str(json.loads(msg)["nodeAddr"])
	router_deviceCount=int(json.loads(msg)["router_deviceCount"])
	deviceAddr= str(json.loads(msg)["deviceAddr"])
	rssi=int(json.loads(msg)["rssi"])
	tagType = str(json.loads(msg)["tagType"])
	version = str(json.loads(msg)["version"])
	MrapFrameCount= int(json.loads(msg)["MrapFrameCount"])
	moistureIndex = int(json.loads(msg)["Index"])
	Temperature =int(json.loads(msg)["Temperature"])
	uvPower = float(json.loads(msg)["uvPower"])
	VisibleLightPower = float(json.loads(msg)["VisibleLightPower"])
	router_major=int(json.loads(msg)["router_major"])
	router_minor=int(json.loads(msg)["router_minor"])

	conn = sqlite3.connect('bleSensor.db') #create a connection to database
	a = conn.cursor()
	a.execute("CREATE TABLE IF NOT EXISTS smartMoistureProbe (timestampUTC str,routerMac str, devType int,routerTL str,routerTLid str,"
	"routerLat float, routerLong float, nodeAddr str, routerDeviceCount int, deviceAddress str, rssi int, tagType str, version str,"
	"MRAPFrameCount int, moistureIndex int, temperature int, uvPower float, visibleLightPower float, routerMajor int, routerMinor int)")

	a.execute("INSERT INTO smartMoistureProbe (timestampUTC,routerMac,devType,routerTL,routerTLid,routerLat,routerLong,nodeAddr,routerDeviceCount,"
	"deviceAddress,rssi,tagType,version,MRAPFrameCount,moistureIndex,temperature,uvPower,visibleLightPower,"
	"routerMajor,routerMinor) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(timestampUTC,router_mac,dev_type,router_tl,router_tlid,
	router_lat,router_long,nodeAddr,router_deviceCount,deviceAddr,rssi,tagType,version,MrapFrameCount,moistureIndex,Temperature,
	uvPower,VisibleLightPower,router_major,router_minor)) #Insert a row of data

	conn.commit() #save the changes
	conn.close() #close the connection to the db
	#client.publish("SmartMoistureProbe/Index", Index)

def selectTagToPub(tagType,client,msg):
	tagList[tagType](client,msg)

client = mqtt.Client()

tagList = {
        "EnvironmentSensor": is_EnvironmentSensor,
        "SmartMoistureProbe": is_SmartMoistureProbe
}
client.on_connect = on_connect
client.on_message = on_message
print ("connecting to broker")
client.connect(broker_address) #connect to broker
print ("Publishing message to topic","console/cmd")
#postInterval_scanDuration="{\"postInterval\":\"300000\",\"scanDuration\":\"300000\"}"
postInterval_scanDuration="{\"postInterval\":\"60000\",\"scanDuration\":\"60000\"}"
client.publish("console/cmd",postInterval_scanDuration) #set post interval (scan for 5 minutes , post every 5 minutes
client.loop_forever()
