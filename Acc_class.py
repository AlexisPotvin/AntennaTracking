import sys, getopt

sys.path.append('.')
import RTIMU
import os.path
import time
import math
import threading
import Acc

#IMU init
class Accel (threading.Thread):
	
	def __init__(self):
		threading.Thread.__init__(self)
		self.roll = 0
		self.yaw = 0
		self.pitch = 0
		self.kill = False
		
	def run(self):
		try:
			while True:
				fusionPose=Acc.ReadSingleIMU()
					self.roll = math.degrees(fusionPose[0])
					self.pitch = math.degrees(fusionPose[1])
					self.yaw = math.degrees(fusionPose[2])
					if self.kill == True:
						break
					
		except KeyboardInterropt:
			 pass
				  

