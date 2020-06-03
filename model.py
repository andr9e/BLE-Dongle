from peewee import *

db = SqliteDatabase('bletag.db')

class environmentSensor (Model):
	timestampUTC = TextField()
	routerMac = TextField()
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
		database = db # This model uses the "ble.db" database.

class environmentSensorData (object):
	
	def __init__(self):
		db.connect()
		db.create_tables([environmentSensor],safe = True)
	
	def define_sensor (self,timestampUTC, routerMac, routerLat, routerLong, rssi,temperature, 
	humidity, visibleLightPower, uvPower, pressure, deviceAddress,MRAPFrameCount, 
	routerDeviceCount, routerMajor, routerMinor):
		environmentSensor.create(timestampUTC=timestampUTC, router_mac=routerMac,
		router_lat=routerLat,router_long=routerLong, rssi=rssi,Temperature=temperature,
		Humidity=humidity,Lux=visibleLightpower, uvPower=uvPower, pressure=pressure, 
		deviceAddr=deviceAddress,MrapFrameCount=MRAPFrameCount,router_deviceCount=routerDeviceCount,
		router_major=routerMajor, router_minor=routerMinor)
	
	def close (self):
		db.close()

