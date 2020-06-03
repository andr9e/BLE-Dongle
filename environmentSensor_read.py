import model

data = model.environmentSensorData()
#data2= model.testClassData()
data.define_sensor("timestampt","tests",33.2,33.2,22,44,43,456.4,22.3,33.4,"devaddress",33,33,2,1)
#data2.define_sensor("henry",55)
data.close()
