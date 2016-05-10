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
uav.set_telemetry_IP("")
uav.set_telemetry_port(5006)
uav.create_bind_socket()

print  "bind done"
"""
#init Antenna Gps coordinates
antennaGps.GPS_coordinate_avg(6)
antenna.antennaLat = antennaGps.lat
antenna.antennaLon = antennaGps.lon
antenna.antennaAlt = antennaGps.alt
"""
antenna.antennaLat = 49.9156538
antenna.antennaLon = -98.2731521
antenna.antennaAlt = 263.624
#time.sleep(20)

print "shoould be calculating"
Acc.ReadImu(antenna,5)
antenna.Orientationoffset(antenna.yaw)
print "alt", antenna.antennaAlt, "lon:", antenna.antennaLon,"lat", antenna.antennaLat
print "offset", antenna.bearingoffset

while True:
	print "antennaalt", antenna.antennaAlt	
	uav.recieve_telemetry()
    	uav.update_UAVgps()
	uav.update_UAVAttitude()
#	print 'uav lat', uav.lat, 'uavlong', uav.lon, 'uav.alt',uav.alt
	#print 'uav', uav.roll
    	#read current position
	#Acc.emptyIMUBuff()
	Acc.ReadImu(antenna,2)
	#update th gps coordinate of the uav
	antenna.uavLat = uav.lat
	antenna.uavAlt = uav.alt
	antenna.uavLon = uav.lon
	#update the wanted angles
	antenna.updateYawFromGPS()
	antenna.updatePitchFromGPS()
	#set the antenna to the correcte angle
	#antenna.angleoffsetcalc()
	#print 'antenna pitch', antenna.pitch
	tickyaw=YawServo.Refresh(antenna.wyaw,antenna.yaw)
	tickpitch=PitchServo.Refresh(antenna.wpitch,antenna.pitch)
	print "yawtick",tickyaw, "Pitchticks", tickpitch
	print "wyaw", antenna.wyaw, "yaw", antenna.yaw, "wpitch", antenna.wpitch , "pitch", antenna.pitch
	print "new ite"
#	time.sleep(0.1)
