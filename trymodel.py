import model
import json

environmentsensor_data_msg = {
    "timestampUTC":"04/06/2020 15:22:16",
    "router_mac":"90E202CDB165",
    "dev_type":"0",
    "router_tl":"USB",
    "router_tlid":"",
    "router_lat":"28.5831322",
    "router_long":"-81.2936732",
    "nodeAddr":"90E202CDB165",
    "router_deviceCount":"2","deviceAddr":
    "90E202CD4492",
    "rssi":"-70",
    "tagType":"EnvironmentSensor",
    "version":"Firmware: 1, Hardware: 0",
    "MrapFrameCount":"7342",
    "Humidity":"64",
    "Temperature":"25",
    "uvPower":"0",
    "VisibleLightPower":"15475.2",
    "Pressure":"101.9438",
    "router_major":"1",
    "router_minor":"2"
}
msg =json.dumps(environmentsensor_data_msg)
#msg = '{"timestampUTC":"04/06/2020 15:07:06","router_mac":"90E202CDB165","dev_type":"0","router_tl":"USB","router_tlid":"","router_lat":"28.5831322","router_long":"-81.2936732","nodeAddr":"90E202CDB165","router_deviceCount":"2","deviceAddr":"44EAD823FBD2","rssi":"-67","tagType":"SmartMoistureProbe","version":"Firmware: 0, Hardware: 0","MrapFrameCount":"1424","Index":"3722","Temperature":"26","uvPower":"0","VisibleLightPower":"33830.4","router_major":"1","router_minor”:”2”}'
#data = model.environmentSensorData()
data = model.environmentSensorData()
#data2= model.testClassData()
#data.define_sensor("timestampt","tests",33.2,33.2,22,44,43,456.4,22.3,33.4,"devaddress",33,33,2,1)
#data2.define_sensor("henry",55)
#data.define_sensor("5-30-22 24:55","123abc",0,"routertl","routerTLid",44.5,44.3,"nodeAddr",
#2,"deviceaddress",-79,"tagType","version",2344,3322,56,44.5,44.6,55,55)
data.define_sensor(msg)
data.close()
