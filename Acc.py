#--coding: utf-8--
import sys, getopt

sys.path.append('.')
import RTIMU
import os.path
import time
import math

k=0
if k==0:
	SETTINGS_FILE = "RTIMULib"

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

# this is a good time to set any fusion parameters 

	imu.setSlerpPower(0.02)
	imu.setGyroEnable(True)
	imu.setAccelEnable(True)
	imu.setCompassEnable(True)

	poll_interval = imu.IMUGetPollInterval()
	print("Recommended Poll Interval: %dmS\n" % poll_interval)

	k=1

def ReadImu(accel,x):

	r=0
	p=0
	y=0
	i=0
	#Faire une moyenne des x  données
	while i < x :
		if imu.IMURead():
	
			data = imu.getIMUData()
			fusionPose = data["fusionPose"]
			"""print("r: %f p: %f y: %f" %(math.degrees(fusionPose[0]),
			math.degrees(fusionPose[1]),math.degrees(fusionPose[2])))"""
	
			r= r+ math.degrees(fusionPose[0])			
			p= p+ math.degrees(fusionPose[1])
			y= y+ math.degrees(fusionPose[2])
			i = i+1
	

	accel.roll= r/x
	accel.pitch= p/x
	accel.yaw= y/x

	return 1		
	

