import model
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
	select_tag(json.loads(msg.payload)["tagType"],client,msg.payload)

def is_environmentsensor(client,msg):
	print (msg)
	data = model.environmentSensorData()
	data.define_sensor(msg)
	data.close()

def is_smartmoistureprobe(client, msg):
	print (msg)
	data = model.smartMoistureProbeData()
	data.define_sensor(msg)
	data.close()

def select_tag(tagType,client,msg):
	tagList[tagType](client,msg)

client = mqtt.Client()

tagList = {
        "EnvironmentSensor": is_environmentsensor,
        "SmartMoistureProbe": is_smartmoistureprobe
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
