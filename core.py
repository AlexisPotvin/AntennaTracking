import Acc
from myclass import Antenna
import servo
import time

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
	
	
