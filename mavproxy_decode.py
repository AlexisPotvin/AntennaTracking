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
        if float(jsonStr['packet_id']) == 33:
            self.alt = float(jsonStr['alt'])
            self.lat = float(jsonStr['lat'])
            self.long = float(jsonStr['lon'])



