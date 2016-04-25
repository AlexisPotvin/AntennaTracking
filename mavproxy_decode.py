__author__ = 'User'

import json
import threading
import udp

class UAVgps(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.lat = 0
        self.alt = 0
        self.long = 0
        self.data  = None
    def uav_altitude(self):
        return self.alt

    def uav_latitude(self):
        return self.lat

    def uav_longitude(self):
        return self.long

    def decode_data(self, data):
        jsonStr = json.loads(data)
        if jsonStr['packet_id'] == 33:
            self.alt = jsonStr['alt']
            self.lat = jsonStr['lat']
            self.long = jsonStr['lon']

x = UAVgps
data = '{"packet_id" : "33", "alt" : "2", "lat" : "3", "lon" : "3"}'
x.decode_data(data)

