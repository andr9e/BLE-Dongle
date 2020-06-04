from peewee import *
import json

db = SqliteDatabase('bletag.db')

class environmentSensor (Model):
	timestampUTC = TextField()
	routerMac = CharField()
	routerLat = FloatField()
	routerLong =FloatField()
	rssi = IntegerField()
	temperature = IntegerField()
	humidity = IntegerField()
	visibleLightPower = FloatField()
	uvPower = FloatField()
	pressure = FloatField()
	deviceAddress = TextField()
	MRAPFrameCount = IntegerField()
	routerDeviceCount = IntegerField()
	routerMajor = IntegerField()
	routerMinor = IntegerField()

	class Meta:
		database = db # This model uses the "bletag.db" database.

class environmentSensorData (object):

	def __init__(self):
		db.connect()
		db.create_tables([environmentSensor],safe = True)

	def define_sensor (self,msg):
		timestampUTC = str(json.loads(msg)["timestampUTC"])
		routerMac =str(json.loads(msg)["router_mac"])
		routerLat=float(json.loads(msg)["router_lat"])
		routerLong=float(json.loads(msg)["router_long"])
		rssi=int(json.loads(msg)["rssi"])
		temperature =int(json.loads(msg)["Temperature"])
		humidity =int(json.loads(msg)["Humidity"])
		visibleLightPower = float(json.loads(msg)["VisibleLightPower"])
		uvPower = float(json.loads(msg)["uvPower"])
		pressure=float(json.loads(msg)["Pressure"])
		deviceAddress=str(json.loads(msg)["deviceAddr"])
		MRAPFrameCount= int(json.loads(msg)["MrapFrameCount"])
		routerDeviceCount=int(json.loads(msg)["router_deviceCount"])
		routerMajor=int(json.loads(msg)["router_major"])
		routerMinor=int(json.loads(msg)["router_minor"])

		environmentSensor.get_or_create(timestampUTC=timestampUTC, routerMac = routerMac,
		routerLat=routerLat,routerLong=routerLong, rssi=rssi,temperature=temperature,
		humidity=humidity,visibleLightPower=visibleLightPower, uvPower=uvPower, pressure=pressure,
		deviceAddress=deviceAddress,MRAPFrameCount=MRAPFrameCount,routerDeviceCount=routerDeviceCount,
		routerMajor=routerMajor, routerMinor=routerMinor)


	def close (self):
		db.close()

class smartMoistureProbe (Model):
	timestampUTC = TextField()
	routerMac = TextField()
	devType = IntegerField()
	routerTL = TextField()
	routerTLid=TextField()
	routerLat= FloatField()
	routerLong=FloatField()
	nodeAddress = TextField()
	routerDeviceCount = IntegerField()
	deviceAddress=TextField()
	rssi = IntegerField()
	tagType=TextField()
	version = TextField()
	MRAPFrameCount=IntegerField()
	moistureIndex=IntegerField()
	temperature= IntegerField()
	uvPower=FloatField()
	visibleLightPower=FloatField()
	routerMajor=IntegerField()
	routerMinor=IntegerField()

	class Meta:
		database = db # This model uses the "bletag.db" database.

class smartMoistureProbeData (object):
	def __init__(self):
		db.connect()
		db.create_tables([smartMoistureProbe],safe = True)

	def define_sensor (self,msg):
		timestampUTC = str(json.loads(msg)["timestampUTC"])
		routerMac = str(json.loads(msg)["router_mac"])
		devType = int(json.loads(msg)["dev_type"])
		routerTL = str(json.loads(msg)["router_tl"])
		routerTLid = str(json.loads(msg)["router_tlid"])
		routerLat= float(json.loads(msg)["router_lat"])
		routerLong= float(json.loads(msg)["router_long"])
		nodeAddress = str(json.loads(msg)["nodeAddr"])
		routerDeviceCount=int(json.loads(msg)["router_deviceCount"])
		deviceAddress= str(json.loads(msg)["deviceAddr"])
		rssi=int(json.loads(msg)["rssi"])
		tagType = str(json.loads(msg)["tagType"])
		version = str(json.loads(msg)["version"])
		MRAPFrameCount= int(json.loads(msg)["MrapFrameCount"])
		moistureIndex = int(json.loads(msg)["Index"])
		temperature =int(json.loads(msg)["Temperature"])
		uvPower = float(json.loads(msg)["uvPower"])
		visibleLightPower = float(json.loads(msg)["VisibleLightPower"])
		routerMajor=int(json.loads(msg)["router_major"])
		routerMinor=int(json.loads(msg)["router_minor"])

		smartMoistureProbe.get_or_create(timestampUTC=timestampUTC,routerMac=routerMac, devType=devType,
		routerTL=routerTL,routerTLid=routerTLid,routerLat=routerLat,routerLong=routerLong,
		nodeAddress=nodeAddress,routerDeviceCount=routerDeviceCount,deviceAddress=deviceAddress,
		rssi=rssi,tagType=tagType,version=version,MRAPFrameCount=MRAPFrameCount,
		moistureIndex=moistureIndex,temperature=temperature,uvPower=uvPower,
		visibleLightPower=visibleLightPower,routerMajor=routerMajor,routerMinor=routerMinor)

	def close (self):
		db.close()
