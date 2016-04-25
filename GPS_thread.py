import threading
import gps
import os

class UartGPS(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        os.system("killall gpsd")
        os.system("sudo gpsd /dev/tty/AMA0 -F /var/run/gpsd.sock")
        self.gpssession = gps.gps("localhost", "2947")
        self.gpssession.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
        self.lat = 0
        self.alt = 0
        self.long = 0

    def update_GPS_coordinates(self):
        try:
            report = self.gpssession.next()
            if report['class'] == 'TPV':
                if hasattr(report, 'alt'):
                    self.alt = report.alt
                if hasattr(report, 'lon'):
                    self.long = report.lon
                if hasattr(report, 'lat'):
                    self.lat = report.lat

        except KeyError:
            pass
        except StopIteration:
            self.gpssession = None
            print "GPS has terminated"

    def GPS_coordinate_avg(self, nb_iterations):
        alt_nb_value = 0
        lon_nb_value = 0
        lat_nb_value = 0
        alt_temp = 0
        lon_temp = 0
        lat_temp = 0

        for i in range(nb_iterations):
            try:
                report = self.gpssession.next()
                if report['class'] == 'TPV':
                    if hasattr(report, 'alt'):
                        alt_temp += report.alt
                        alt_nb_value += 1

                    if hasattr(report, 'lon'):
                        lon_temp += report.lon
                        lon_nb_value += 1

                    if hasattr(report, 'lat'):
                        lat_temp += report.lat
                        lat_nb_value += 1

            except KeyError:
                pass
            except StopIteration:
                self.gpssession = None
                print "GPS has terminated"
        try:
            self.lat = lat_temp / lat_nb_value
        except ZeroDivisionError:
            print "Lat_div_0"
        try:
            self.long = lon_temp / lon_nb_value
        except ZeroDivisionError:
            print "Lon_div_0"
        try:
            self.alt = alt_temp / alt_nb_value
        except ZeroDivisionError:
            print "alt_div_0"

    def current_altitude(self):
        return self.alt

    def current_latitude(self):
        return self.lat
    def current_longitude(self):
        return self.long
