import sys, getopt

sys.path.append('.')
import RTIMU
import os.path
import time
import math
import threading

#IMU init
class Accel (threading.Thread):
	
	def __init__(self):
		threading.Thread.__init__(self)
		SETTINGS_FILE = "RTIMULib" #Init file name
		print ("Using settings file" +  SETTINGS_FILE +  ".ini")
		if not os.path.exists(SETTINGS_FILE + ".ini"):
        		print("Settings file does not esist, will be created")
		s = RTIMU.Settings(SETTINGS_FILE)
		imu = RTIMU.RTIMU(s)
		print ("IMU Name : " + imu.IMUName())
		if (not imu.IMUInit()):
		        print ("IMU Init Failed")
		        sys.exit(1)
		else:
		        print("IMU Init Succeeded")
		imu.setSlerpPower(0.02)
		imu.setGyroEnable(True)
		imu.setAccelEnable(True)
		imu.setCompassEnable(True)
		poll_interval = imu.IMUGetPollInterval()
		print("Recommended Poll Interval: %dmS\n" % poll_interval)
		self.imu = imu
	
	def run(self):
		while True:
			try: 
				print "alors la force g ca se calcul avec un imu"
				time.sleep(1)
				if self.imu.IMURead():
					data = self.imu.getIMUData()
					fusionPose = data["fusionPose"]
					self.roll = math.degrees(fusionPose[0])
					self.pitch = math.degrees(fusionPose[1])
					self.yaw = math.degrees(fusionPose[2])
			except KeyboardInterropt:
				print "test"
				pass
				  

