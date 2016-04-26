
import Acc
from antenna_class import Antenna
from servo_class import NewServo
import servo
import time
from keyboard import KBHit
from mavproxy_decode import UAVgps
from GPS_thread import UartGPS



#classkbhit contains actions relatives to the keyboard
kb=KBHit()

antenna = Antenna()
#defien both the servos
YawServo = NewServo(-180,180,1.1,1.9,1.5,100,0,3)
PitchServo = NewServo(0,90,1.1,1.9,1.5,100,1,1)

antennaGps = UartGPS()

uav = UAVgps()
uav.set_telemetry_IP("127.0.0.1")
uav.set_telemetry_port(5005)
uav.create_bind_socket()
print  "bind done"

#init Antenna Gps coordinates
antennaGps.GPS_coordinate_avg(10)
antenna.antennaLat = antennaGPS.lat
antenna.antennaLon = antennaGPS.lon
antenna.antennaAlt = antennaGps.alt

Acc.ReadImu(antenna,5)
antenna.orientationoffset(antenna.yaw)

while True:
	
	uav.recieve_telemetry()
    	uav.update_UAVgps()
    	#read current position
	Acc.ReadImu(antenna,5)
	#update th gps coordinate of the uav
	antenna.uavLat = uav.lat
	antenna.uavAlt = uav.alt
	antenna.uavLon = uav.lon
	#update the wanted angles
	antenna.upateYawFromGPS()
	antenna.updatePitchFromGPS()
	#set the antenna to the correcte angle
	antenna.angleoffsetcalc()
	tickyaw=YawServo.Refresh(antenna.wyaw,antenna.yaw)
	tickpitch=PitchServo.Refresh(antenna.wpitch,antenna.pitch)
	print "yawtick",tickyaw, "Pitchticks", tickpitch
	
	"""
	arrowcode = -1

	if kb.kbhit():
		arrowcode = kb.getarrow()
		print "hello", arrowcode
	"""
	
	antenna.arrow(arrowcode)	
