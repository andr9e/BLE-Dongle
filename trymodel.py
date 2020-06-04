import model

#data = model.environmentSensorData()
data = model.smartMoistureProbeData()
#data2= model.testClassData()
#data.define_sensor("timestampt","tests",33.2,33.2,22,44,43,456.4,22.3,33.4,"devaddress",33,33,2,1)
#data2.define_sensor("henry",55)
data.define_sensor("5-30-22 24:55","123abc",0,"routertl","routerTLid",44.5,44.3,"nodeAddr",
2,"deviceaddress",-79,"tagType","version",2344,3322,56,44.5,44.6,55,55)
data.close()
