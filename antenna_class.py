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
    		
    
	
