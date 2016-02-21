import gps

#Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.steam(gps.WATCH_ENABLE|gps.WATCH_NEWSTYLE)

while True:
	try:
		report = session.ext()
	
	#WAIT FOR A 'TPV' report and display the current time 

#	print report
	
		if report['class'] == 'TPV':
			if hasattr(report, 'time'):
				print report.time

	except KeyError:
pass
	except KeyboardInterrupt :
quit()
	except StopIteration:
session = None
print "GPSD has terminated"
