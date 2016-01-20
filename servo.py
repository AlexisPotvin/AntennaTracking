

import time
import sys
sys.path.append('Adafruit/Adafruit_PWM_Servo_Driver')
import Adafruit_PWM_Servo_Driver as pwm



def setServoPulse(channel, pulse):
  print pulse 
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 100                       # 100 Hz
  #print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  #print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  print pulse
  pulse = round(pulse,0)
  pwm.setPWM(channel, 0, pulse)
  print "Les pulse sont :", pulse
pwm =pwm.PWM(0x41)
pwm.setPWMFreq(100)


channel_yaw = 0
channel_pitch = 1

yaw_up = 700
yaw_hold = 614
yaw_down = 550

pitch_up = 700
pitch_hold = 614
pitch_down = 550

def update(yaw,pitch):
	if yaw == 'up':
		pwm.setPWM(channel_yaw,0, yaw_up)
	elif yaw == 'down':
		pwm.setPWM(channel_yaw,0, yaw_down)
	elif yaw == 'hold':
                pwm.setPWM(channel_yaw,0, yaw_hold)
#		print "Victor est le plus nul !!"
	else:
		pwm.setPWM(channel_yaw,0, yaw_hold)
	
	if pitch == 'up':
                pwm.setPWM(channel_pitch,0, pitch_up)
        elif pitch == 'down':
                pwm.setPWM(channel_pitch,0, pitch_down)
        elif pitch == 'hold':
                pwm.setPWM(channel_pitch,0, pitch_hold)
#        	print "Abde est le plus nul !!"

	else:
                pwm.setPWM(channel_pitch,0, pitch_hold)
	
def RefreshServo (tickvalue,channel):

	pwm.setPWM(channel,0,tickvalue)

