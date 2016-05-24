class gpsreader():
	def __init__(self,path):
		self.path = path
		self.Lat = 0
		self.Lon = 0
		self.Alt = 0

	def readgps(self):
		with open (self.path) as f:
			for line in f:
				numbers_float = map(float, line.split())
				self.Lat = numbers_float[0]
				self.Lon = numbers_float[1]
				self.Alt = numbers_float[2]
	
		
