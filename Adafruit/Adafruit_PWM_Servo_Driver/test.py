from   Adafruit_PWM_Servo_Driver import PWM
import time 


pwm = PWM(0x41)

pwm.setPWMFreq(100)
while(True):
	pwm.setPWM(0,0,787)
	time.sleep(1)
	




