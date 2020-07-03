from peewee import *
from playhouse.sqlite_ext import *
import json
import datetime

db = SqliteExtDatabase('tag.db')

class BaseModel (Model):
	class Meta:
		database = db

class Room (BaseModel):
	name = CharField(primary_key=True)
	create_date = DateTimeField()

class RoomData():

	def create_room(self,room):
		db.connect()
		db.create_tables([Room],safe = True)
		Room.get_or_create(name=room,create_date=datetime.datetime.now())
		db.close()

	def delete_room(self,name):
		db.connect()
		delete_room=Room.delete().where(Room.name == name)
		delete_room.execute()
		db.close()

	def room_count(self):
		db.connect()
		return Room.select().count()
		db.close()


class KnownTag (BaseModel):
	room = ForeignKeyField(Room)
	tag_name = CharField()
	tag_type = CharField()
	tag_id = CharField(primary_key=True)	# device MAC ID
	create_date = DateTimeField()

class KnownTagData():
	def define_tag(self,tag_room,tag_name,tag_type,tag_id):
		db.connect()
		db.create_tables([KnownTag],safe = True)
		KnownTag.get_or_create (room = Room.get(Room.name == tag_room),
		tag_name=tag_name,tag_type=tag_type,tag_id=tag_id,
		create_date=datetime.datetime.now())
		db.close()

	def get_tag(self):
		db.connect()
		for known_tag in KnownTag.select():
			print (known_tag.room.name)

		db.close()

class Tag(BaseModel):
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
	data = JSONField()

class TagData():
	def __init__(self,msg):
		db.connect()
		db.create_tables([Tag],safe = True)

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
		routerMajor=int(json.loads(msg)["router_major"])
		routerMinor=int(json.loads(msg)["router_minor"])


		Tag.get_or_create(
		timestampUTC=timestampUTC,
		routerMac = routerMac,
		devType=devType,
		routerTL=routerTL,
		routerTLid=routerTLid,
		routerLat=routerLat,
		routerLong=routerLong,
		nodeAddress=nodeAddress,
		routerDeviceCount=routerDeviceCount,
		deviceAddress=deviceAddress,
		rssi=rssi,
		tagType=tagType,
		version=version,
		MRAPFrameCount=MRAPFrameCount,
		routerMajor=routerMajor,
		routerMinor=routerMinor,
		data=msg)

		db.close()



class environmentSensor (BaseModel):
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
	temperature = IntegerField()
	humidity = IntegerField()
	visibleLightPower = FloatField()
	uvPower = FloatField()
	pressure = FloatField()


class environmentSensorData ():

	def __init__(self,msg):
		db.connect()
		db.create_tables([environmentSensor],safe = True)

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
		routerMajor=int(json.loads(msg)["router_major"])
		routerMinor=int(json.loads(msg)["router_minor"])
		temperature =int(json.loads(msg)["Temperature"])
		humidity =int(json.loads(msg)["Humidity"])
		visibleLightPower = float(json.loads(msg)["VisibleLightPower"])
		uvPower = float(json.loads(msg)["uvPower"])
		pressure=float(json.loads(msg)["Pressure"])


		environmentSensor.get_or_create(
		timestampUTC=timestampUTC,
		routerMac = routerMac,
		devType=devType,
		routerTL=routerTL,
		routerTLid=routerTLid,
		routerLat=routerLat,
		routerLong=routerLong,
		nodeAddress=nodeAddress,
		routerDeviceCount=routerDeviceCount,
		deviceAddress=deviceAddress,
		rssi=rssi,
		tagType=tagType,
		version=version,
		MRAPFrameCount=MRAPFrameCount,
		routerMajor=routerMajor,
		routerMinor=routerMinor,
		temperature=temperature,
		humidity=humidity,
		visibleLightPower=visibleLightPower,
		uvPower=uvPower,
		pressure=pressure)

		db.close() #close database connection

class smartMoistureProbe (BaseModel):
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
	moistureIndex=IntegerField()
	temperature= IntegerField()
	uvPower=FloatField()
	visibleLightPower=FloatField()

class smartMoistureProbeData ():
	def __init__(self,msg):
		db.connect()
		db.create_tables([smartMoistureProbe],safe = True)

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
		routerMajor=int(json.loads(msg)["router_major"])
		routerMinor=int(json.loads(msg)["router_minor"])
		moistureIndex = int(json.loads(msg)["Index"])
		temperature =int(json.loads(msg)["Temperature"])
		uvPower = float(json.loads(msg)["uvPower"])
		visibleLightPower = float(json.loads(msg)["VisibleLightPower"])

		smartMoistureProbe.get_or_create(
		timestampUTC=timestampUTC,
		routerMac=routerMac,
		devType=devType,
		routerTL=routerTL,
		routerTLid=routerTLid,
		routerLat=routerLat,
		routerLong=routerLong,
		nodeAddress=nodeAddress,
		routerDeviceCount=routerDeviceCount,
		deviceAddress=deviceAddress,
		rssi=rssi,
		tagType=tagType,
		version=version,
		MRAPFrameCount=MRAPFrameCount,
		routerMajor=routerMajor,
		routerMinor=routerMinor,
		moistureIndex=moistureIndex,
		temperature=temperature,
		uvPower=uvPower,
		visibleLightPower=visibleLightPower)

		db.close() #close database connection
