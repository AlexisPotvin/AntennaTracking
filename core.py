import Acc
from myclass import Antenna
from myclass import *
import servo
import time
import arrows
Antenna = Antenna()
YawServo = NewServo(-180,180,1.1,1.9,1.5,100,0)
PitchServo = NewServo(0,90,1.1,1.9,1.5,100,1)

YawServo.Refresh(2,10)
while True:


	Acc.ReadImu(Antenna,5)
	arrows.get(Antenna)
	tickyaw=YawServo.Refresh(Antenna.wyaw,Antenna.yaw)
	tickpitch=PitchServo.Refresh(Antenna.wpitch,Antenna.pitch)
	print "yawtick",tickyaw, "Pitchticks", tickpitch

"""
	#Acc.ImuInit()
while True:
	Acc.ReadImu(Antenna,5)
	print Antenna.roll, Antenna.pitch, Antenna.yaw 

while True :
	print "Hold"
	servo.update("hold","hold")
	time.sleep(1)
	print "up"
 	servo.update("up","up")
	time.sleep(2)
	print "hold"
	servo.update("hold","hold")
        time.sleep(1)
	print "down"
        servo.update("down","down")
	time.sleep(2)
	print "Je suis rendu"
	
	
"""
