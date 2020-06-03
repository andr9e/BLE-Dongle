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
		environmentSensor.create(timestampUTC=timestampUTC, routerMac = routerMac,
		routerLat=routerLat,routerLong=routerLong, rssi=rssi,temperature=temperature,
		humidity=humidity,visibleLightPower=visibleLightPower, uvPower=uvPower, pressure=pressure, 
		deviceAddress=deviceAddress,MRAPFrameCount=MRAPFrameCount,routerDeviceCount=routerDeviceCount,
		routerMajor=routerMajor, routerMinor=routerMinor)
	
	def close (self):
		db.close()

class smartMoistureProbe (Model):
	timestampUTC = TextField()
	routerMac = TextField()
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

