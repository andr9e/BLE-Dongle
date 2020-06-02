from peewee import *

db = SqliteDatabase('ble.db')

class enviornmentSensor(Model):
	timestampUTC = TextField()
	routerMac = TextField()
	routerLat = FloatField()
	routerLong = FLoatField()
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
		database = ble # This model uses the "ble.db" database.
