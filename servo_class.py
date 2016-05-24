import math
import servo
import calcul
from UAVclass import UAV

def adafruitpwmvalue(pwmvalue, pwmfrequency):
        pulse = pwmvalue *1000
        pulse = pulse/1000000
        pulse = pulse * pwmfrequency
        pulse = pulse *4096

        pulse = int(pulse)
        return pulse


def getdelta(x1,y1,x2,y2):
        slope = float(y2 - y1) / float(x2-x1)
        return slope

def GetY(initval,slope,xval,mul):
	y = 0
	y = (slope * mul)  * xval
	y = y+initval
	y = math.fabs(y)
	return int(y)
		
class NewServo():

	def __init__(self,minangle,maxangle,minpwm,maxpwm,holdpwm,servofreq,channel,mul):
		self.delta = getdelta(maxangle,adafruitpwmvalue(maxpwm,servofreq),minangle,adafruitpwmvalue(minpwm,servofreq))
		self.init= adafruitpwmvalue(holdpwm,servofreq)
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
		self.multiplicator = mul
		
	#resposible to reflesing the servo to a certain directiron
	def Refresh (self,WantedAngle , CurrentAngle):
		AngleCorrection = (WantedAngle - CurrentAngle)
		if abs(AngleCorrection) >= self.Angletolerance :
			ticks = GetY(self.init, self.delta,AngleCorrection,self.multiplicator)
			servo.RefreshServo(ticks,self.channel)					
		else :
			ticks = adafruitpwmvalue(self.holdpwm,self.servofreq)
			servo.RefreshServo(ticks,self.channel)
		return ticks		
#x = NewServo(0,90,1.2,1.5,1.9,100,0)





#adafruitpwmvalue(1.9,100)

