
import Acc
from antenna_class import Antenna
from servo_class import NewServo
import servo
import time
from keyboard import KBHit

#classkbhit contains actions relatives to the keyboard
kb=KBHit()
#antenna contains the basics info about the antenna
Antenna = Antenna()
#defien both the servos
YawServo = NewServo(-180,180,1.1,1.9,1.5,100,0,3)
PitchServo = NewServo(0,90,1.1,1.9,1.5,100,1,1)

YawServo.Refresh(2,10)
while True:

	arrowcode = -1

	if kb.kbhit():
		arrowcode = kb.getarrow()
		print "hello", arrowcode

	Acc.ReadImu(Antenna,5)
	Antenna.arrow(arrowcode)
	tickyaw=YawServo.Refresh(Antenna.wyaw,Antenna.yaw)
	tickpitch=PitchServo.Refresh(Antenna.wpitch,Antenna.pitch)
	print "yawtick",tickyaw, "Pitchticks", tickpitch

