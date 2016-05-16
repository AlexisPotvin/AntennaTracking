from Acc_class import Accel
import time

x = Accel()
x.start()
try:

	while True:
		time.sleep(1)
		print "hello"
		#print x.pitch, x.yaw
except KeyboardInterrupt:
	print "nick ta mere"
	x.join(1)	
