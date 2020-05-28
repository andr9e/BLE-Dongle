import json
import unicodedata
import mysql.connector

class Decoder(json.JSONDecoder):
	def decode(self, s):
		result = super().decode(s) # result = super(Decoder, self).decode(s)
		return self._decode(result)
	
	def _decode(self, o):
		if isinstance(o, str) or isinstance(o, unicodedata):
			try:
				return int(o)
			except ValueError:
				return o
		elif isinstance(o, dict):
			return {k: self._decode(v) for k, v in o.items()}
		elif isinstance(o, list):
			return [self.decode(v) for v in o]
		else:
			return o
c ='{"value": "42","version":"0","router_mac":"ab5d67654323","timestampUTC":"2/12/20 6:34:06 PM"}'
temp=int(json.loads(c)["value"])
ver= int(json.loads(c)["version"])
router=str(json.loads(c)["router_mac"])
timestampUTC= str(json.loads(c)["timestampUTC"])
db=mysql.connector.connect(host="db-mdrdio-test.cei6tu7boufa.us-east-1.rds.amazonaws.com",port=3300,user="admin",passwd="hemlock2",db="modern_radio_sensors")
if (db):
	print ("connection was successfull")
                #db.close()
else:
	print ("connection failed")
cursor = db.cursor()
sql ="""INSERT INTO environmentsensors (router_mac,Temperature,Humidity,timestampUTC) VALUES (%s,%s,%s,%s)"""
data= (router,temp,77,timestampUTC)
cursor.execute(sql,data)
db.commit()
print (cursor.rowcount, "record inserted.")
db.close()

print (temp)
