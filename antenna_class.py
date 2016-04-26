import calcul

class Antenna():

	def __init__(self):
		self.roll =0
		self.pitch =0
		self.yaw = 0
		self.wyaw = 0
		self.wpitch = 0
		self.bearingoffset = 0
		self.uavAlt = 0
		self.uavLon = 0
		self.uavLat = 0
		self.antennaAlt = 0
		self.antennaLon = 0
		self.antennaLat = 0
		
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
        	
    	def updateYawFromGPS(self):
    		self.wyaw = calcul.bearing(self.antennaLLat, self.antennaLon, self.uavLat, self.uavLon)
    	
    	def updatePitchFromGPs(self):
    		self.wpitch = calcul.pitch(self.antennaLLat, self.antennaLon, self.antennaAlt, self.uavLat, self.uavLon, self.uavAlt)
    		
	
