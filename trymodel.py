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

smartmoitureprobe_Data_msg = {
"timestampUTC":"04/06/2020 15:07:06",
"router_mac":"90E202CDB165",
"dev_type":"0",
"router_tl":"USB",
"router_tlid":"",
"router_lat":"28.5831322",
"router_long":"-81.2936732",
"nodeAddr":"90E202CDB165",
"router_deviceCount":"2",
"deviceAddr":"44EAD823FBD2",
"rssi":"-67",
"tagType":"SmartMoistureProbe",
"version":"Firmware: 0, Hardware: 0",
"MrapFrameCount":"1424",
"Index":"3722",
"Temperature":"26",
"uvPower":"0",
"VisibleLightPower":"33830.4",
"router_major":"1",
"router_minor":"2"
}


msg =json.dumps(environmentsensor_data_msg)
#msg =json.dumps(smartmoitureprobe_Data_msg)
data = model.environmentSensorData()
#data= model.smartMoistureProbeData()
data.define_sensor(msg)
data.close()
