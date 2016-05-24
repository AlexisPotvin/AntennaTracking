import Acc
from antenna_class import Antenna
from servo_class import NewServo
from Acc_class import Accel
import servo
import time
from keyboard import KBHit
from mavproxy_decode import UAVgps
from GPS_thread import UartGPS
import os
from file import gpsreader

anttxt = gpsreader('antgps.txt')
uavtxt = gpsreader('uavgps.txt')

#classkbhit contains actions relatives to the keyboard
kb=KBHit()

antenna = Antenna()
antennaGps = UartGPS()
Accel = Accel()

#defien both the servos
YawServo = NewServo(-180,180,1.1,1.9,1.5,100,0,0.8)
PitchServo = NewServo(0,90,1.1,1.9,1.5,100,1,0.5)



uav = UAVgps()
uav.set_telemetry_IP("")
uav.set_telemetry_port(5006)
uav.create_bind_socket()

print  "bind done"

#init Antenna Gps coordinates
"""
antennaGps.GPS_coordinate_avg(2)
antenna.antennaLat = antennaGps.lat
antenna.antennaLon = antennaGps.lon
antenna.antennaAlt = antennaGps.alt
"""
"""
antenna.antennaLat = 45.4958755
antenna.antennaLon = -73.5633529
antenna.antennaAlt = 20.453
"""
Acc.ReadImu(antenna,5)
antenna.Orientationoffset(antenna.yaw)
#start the imu data 
Accel.start()

while True:

	try:	
		"""
		uav.recieve_telemetry()
                uav.update_UAVgps()
                uav.update_UAVAttitude()
                

		"""

		anttxt.readgps()
		antenna.antennaLat = anttxt.Lat
		antenna.antennaLon = anttxt.Lon
		antenna.antennaAlt = anttxt.Alt
		
		uavtxt.readgps()
		antenna.uavLat = uavtxt.Lat
		antenna.uavLon = uavtxt.Lon
		antenna.uavAlt = uavtxt.Alt
		
		#read current position
		try:
			
			antenna.pitch = Accel.pitch
			antenna.yaw = Accel.yaw
		except :
			pass
#		update th gps coordinate of the uav
		"""
		try:
			antenna.uavLat = uav.lat
			antenna.uavAlt = uav.alt
			antenna.uavLon = uav.lon
		except:
			pass
		"""
		#update the wanted angles
		antenna.updateYawFromGPS()
		antenna.updatePitchFromGPS()

		#set the antenna to the correcte angle
#		antenna.angleoffsetcalc()
		
		tickyaw=YawServo.Refresh(antenna.wyaw,antenna.yaw)
		tickpitch=PitchServo.Refresh(antenna.wpitch,antenna.pitch)
		#print "yawtick",tickyaw, "Pitchticks", tickpitch
		time.sleep(0.2)
		os.system("clear")
		print "UAV Latitude\t", antenna.uavLat
		print "UAV Longitude\t", antenna.uavLon
		print "UAV Altitude\t", antenna.uavAlt
		print "ant Latitude\t", antenna.antennaLat
		print "ant Longitude\t", antenna.antennaLon
		print "ant Altitude\t", antenna.antennaAlt
		print "wanted yaw \t", antenna.wyaw
		print "antenna yaw \t", antenna.yaw
		print "wanted pitch \t", antenna.wpitch
		print "antenna pitch \t", antenna.pitch
		print "yaw tick \t", tickyaw
		print "pitch tick \t", tickpitch

	except (KeyboardInterrupt, SystemExit):
		Accel.kill = True
		raise
