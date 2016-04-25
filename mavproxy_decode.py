__author__ = 'User'

import json
import threading
import socket

class UAVgps(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.lat = 0
        self.alt = 0
        self.long = 0
        self.data = None
        self.telemetryIP = 0
        self.telemetryPort = 0
        self.telemetrySocket = None

    def uav_altitude(self):
        return self.alt

    def uav_latitude(self):
        return self.lat

    def uav_longitude(self):
        return self.long

    def update_UAVgps(self):
        jsonStr = json.loads(data)
        if float(jsonStr['packet_id']) == 33:
            self.alt = float(jsonStr['alt'])
            self.lat = float(jsonStr['lat'])
            self.long = float(jsonStr['lon'])

    def set_telemetry_IP (self, host_IP):
        self.telemetryIP = host_IP

    def set_telemetry_port(self, hostPort):
        self.telemetryPort = hostPort

    def create_bind_socket(self):
        self.telemetrySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        self.telemetrySocket.bind((self.telemetryIP, self.telemetryPort))

    def recieve_telemetry(self):
        self.data, addr = self.telemetrySocket.recvfrom(4096)
