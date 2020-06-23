from peewee import *
import json

db = SqliteDatabase('tag.db')

class BaseModel (Model):
	class Meta:
		database = db

class Room (BaseModel):
	name = CharField()
	create_date = DateTimeField()

class KnownTag (BaseModel):
	room = ForeignKeyField(Room, backref='knowntags')
	tag_name = CharField()
	tag_type = CharField()
	tag_id = CharField()	# device MAC ID
	create_date = DateTimeField()

class BleTag (BaseModel):
	timestampUTC = TextField()
	routerMac = CharField()
	devType = IntegerField()
	routerTL = CharField()
	routerTLid=CharField()
	routerLat = FloatField()
	routerLong =FloatField()
	rssi = IntegerField()
	nodeAddress = CharField()
	routerDeviceCount = IntegerField()
	deviceAddress=CharField()
	tagType=CharField()
	version = TextField()
	MRAPFrameCount=IntegerField()
	routerMajor=IntegerField()
	routerMinor=IntegerField()


class environmentSensor (BleTag):
	temperature = IntegerField()
	humidity = IntegerField()
	visibleLightPower = FloatField()
	uvPower = FloatField()
	pressure = FloatField()


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

		environmentSensor.get_or_create(timestampUTC=timestampUTC, routerMac = routerMac,devType=devType,
		routerTL=routerTL,routerTLid=routerTLid,routerLat=routerLat,routerLong=routerLong,
		nodeAddress=nodeAddress,routerDeviceCount=routerDeviceCount,deviceAddress=deviceAddress,
		rssi=rssi,tagType=tagType,version=version,MRAPFrameCount=MRAPFrameCount,routerMajor=routerMajor,
		routerMinor=routerMinor,temperature=temperature,humidity=humidity,visibleLightPower=visibleLightPower,
		uvPower=uvPower, pressure=pressure)


	def close (self):
		db.close()

class smartMoistureProbe (BleTag):
	moistureIndex=IntegerField()
	temperature= IntegerField()
	uvPower=FloatField()
	visibleLightPower=FloatField()

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
