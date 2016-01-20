import math
import servo

def adafruitpwmvalue(pwmvalue, pwmfrequency):
        pulse = pwmvalue *1000
        pulse = pulse/1000000
        pulse = pulse * pwmfrequency
        pulse = pulse *4096

        pulse = int(pulse)
        return pulse


def getdelta(x1,y1,x2,y2):
        slope = (y2 - y1) /(x2-x1)

        return slope

def GetY(initval,slope,xval):

	y = initval + (slope*xval)
	return y

class Antenna():

	def __init__(self):
		self.roll =0
		self.pitch =0
		self.yaw = 0

class NewServo():

	def __init__(self,minangle,maxangle,minpwm,maxpwm,holdpwm,servofreq,channel):
		self.delta = (maxangle,adafruitpwmvalue(maxpwm,servofreq),minangle,adafruitpwmvalue(minpwm,servofreq))
		self.init =adafruitpwmvalue(holdpwm,servofreq)
		self.currentangle=0
		self.desireangle=0
		self.minpwm = minpwm
		self.maxpwm = maxpwm
		self.holdpwm = holdpwm
		self.minangle=minangle
		self.maxangle=maxangle
		self.servofreq = servofreq
		self.Angletolerance = 5
		self.channel = channel
	def Refresh (WantedAngle,CurrentAngle):
		AngleCorrection = WantedAngle-CurrentAngle
		if abs(AngleCorrection) >= self.Angletolerance :
			ticks = GetY(self.init,self.delta,AngleCorrection)
			servo.RefreshServo(ticks,self.channel)					
		else :
			ticks = adafruitpwmvalue(self.holdpwm,self.servofreq)
			servo.RefreshServo(ticks,self.channel)

x = NewServo(0,90,1.2,1.5,1.9,100,0)




print getdelta(1,2,2,4)
adafruitpwmvalue(1.9,100)

