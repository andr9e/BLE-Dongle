from peewee import *

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

	def define_sensor (self,timestampUTC, routerMac, routerLat, routerLong, rssi,temperature,
	humidity, visibleLightPower, uvPower, pressure, deviceAddress,MRAPFrameCount,
	routerDeviceCount, routerMajor, routerMinor):

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

	def define_sensor (self,timestampUTC,routerMac,devType,routerTL,routerTLid,
	routerLat,routerLong,nodeAddress,routerDeviceCount,deviceAddress,rssi,tagType,version,
	MRAPFrameCount,moistureIndex,temperature,uvPower,visibleLightPower,routerMajor,routerMinor):

		smartMoistureProbe.get_or_create(timestampUTC=timestampUTC,routerMac=routerMac, devType=devType,
		routerTL=routerTL,routerTLid=routerTLid,routerLat=routerLat,routerLong=routerLong,
		nodeAddress=nodeAddress,routerDeviceCount=routerDeviceCount,deviceAddress=deviceAddress,
		rssi=rssi,tagType=tagType,version=version,MRAPFrameCount=MRAPFrameCount,
		moistureIndex=moistureIndex,temperature=temperature,uvPower=uvPower,
		visibleLightPower=visibleLightPower,routerMajor=routerMajor,routerMinor=routerMinor)

	def close (self):
		db.close()

class testClass (Model):
        name = TextField()
        temp = IntegerField()

        class Meta:
                database = db

class testClassData (object):
        def __init__(self):
                db.connect()
                db.create_tables([testClass], safe = True)

        def define_sensor (self,name, temp):
                testClass.get_or_create(name= name,temp=temp)

        def close (self):
                db.close()