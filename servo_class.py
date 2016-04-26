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

def GetY(initval,slope,xval):
	y = 0
	y = slope * xval
	y = y+initval
	return int(y)
""" moved to antenna_class
class Antenna():

	def __init__(self):
		self.roll =0
		self.pitch =0
		self.yaw = 0
		self.wyaw = 0
		self.wpitch = 0
		self.bearingoffset = 0
		self.uav = UAV()
	def arrow (self,arrow) :
		if arrow ==0 :
			self.wpitch +=5
		elif arrow == 1: 
			self.wyaw +=5
		elif arrow == 2:
			self.wpitch -=5
		elif arrow == 3:
			self.wyaw -= 5
	def Orientationoffset (self,bearingoffset):
		self.bearingoffset = bearingoffset
    	def angleoffsetcalc(self):
        	self.yaw = calcul.bearingoffset(self.yaw,self.bearingoffset)
        	self.wyaw = calcul.bearingoffset(self.wyaw,self.bearingoffset)
    	#def GPS_to_angle(self):
    		
 """  
		
class NewServo():

	def __init__(self,minangle,maxangle,minpwm,maxpwm,holdpwm,servofreq,channel,multiplication):
		self.servomultiplication = multiplication
		self.delta = getdelta(maxangle,adafruitpwmvalue(maxpwm,servofreq),minangle,adafruitpwmvalue(minpwm,servofreq))* self.servomultiplication
		self.init= adafruitpwmvalue(holdpwm,servofreq)
		self.currentangle=0
		self.desireangle=0
		self.minpwm = minpwm
		self.maxpwm = maxpwm
		self.holdpwm = holdpwm
		self.minangle=minangle
		self.maxangle=maxangle
		self.servofreq = servofreq
		self.Angletolerance = 2
		self.channel = channel
		
		
	#resposible to reflesing the servo to a certain directiron
	def Refresh (self,WantedAngle , CurrentAngle):
		AngleCorrection = (WantedAngle - CurrentAngle)
		if abs(AngleCorrection) >= self.Angletolerance :
			ticks = GetY(self.init, self.delta,self.servomultiplication)
			servo.RefreshServo(ticks,self.channel)					
		else :
			ticks = adafruitpwmvalue(self.holdpwm,self.servofreq)
			servo.RefreshServo(ticks,self.channel)
		return ticks		
#x = NewServo(0,90,1.2,1.5,1.9,100,0)





#adafruitpwmvalue(1.9,100)

