hor__ = 'User'

import json
import threading
import socket
import math
class UAVgps(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.lat = 0
        self.alt = 0
        self.lon = 0
        self.data = None
        self.telemetryIP = 0
        self.telemetryPort = 0
        self.telemetrySocket = None
        self.time_boot_ms = 0
        self.pitch= 0
        self.yaw = 0
        self.roll = 0
	    self.kill = False

    def uav_altitude(self):
        return self.alt

    def uav_latitude(self):
        return self.lat

    def uav_longitude(self):
        return self.lon

    def update_UAVgps(self):
        jsonStr = json.loads(self.data)
        if float(jsonStr['packet_id']) == 33:
            self.alt = float(jsonStr['alt'])/1000
            self.lat = float(jsonStr['lat'])/10000000
            self.lon = float(jsonStr['lon'])/10000000

    def update_UAVRawgps(self):
        jsonStr = json.loads(self.data)
        if float(jsonStr['packet_id']) == 24:
            self.alt = float(jsonStr['alt'])/1000
            self.lat = float(jsonStr['lat'])/10000000
            self.lon = float(jsonStr['lon'])/10000000

    def update_UAVAttitude(self):
        jsonStr = json.loads(self.data)
        if float(jsonStr['packet_id']) == 30:
            self.time_boot_ms = float(jsonStr['time_boot_ms'])
            self.pitch= math.degrees(float(jsonStr['pitch']))
            self.yaw = math.degrees(float(jsonStr['yaw']))
            self.roll = math.degrees(float(jsonStr['roll']))

    def set_telemetry_IP (self, host_IP):
        self.telemetryIP = host_IP

    def set_telemetry_port(self, hostPort):
        self.telemetryPort = hostPort

    def create_bind_socket(self):
        self.telemetrySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        #self.telemetrySock = socket.socket()
	self.telemetrySocket.bind((self.telemetryIP, self.telemetryPort))

    def recieve_telemetry(self):
        self.data, addr = self.telemetrySocket.recvfrom(4096)

    def run(self):
        try:
            while True:
                self.recieve_telemetry()
                self.update_UAVgps()
                self.update_UAVAttitude()
                self.update_UAVRawgps()
                if self.kill == True:
                        break
        except KeyboardInterrupt:
            self.kill = True








