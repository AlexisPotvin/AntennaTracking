import math


def bearing(lat_sat, long_sat, lat_drone, long_drone):
    lat_sat = math.radians(lat_sat)
    lat_drone = math.radians(lat_drone)
    long_sat = math.radians(long_sat)
    long_drone = math.radians(long_drone)
    delta_long = long_drone - long_sat
    delta_lat = lat_drone - lat_sat
    y = math.sin(delta_long)*math.cos(lat_drone)
    x = math.cos(lat_sat)*math.sin(lat_drone) - \
    math.sin(lat_sat)*math.cos(lat_drone)*math.cos(delta_long)
    #plage de -180 a 180
    bearing_initial = math.degrees(math.atan2(y, x))
    #Pour le mettre dans le plage de 0 a 360
    #bearing_360=(bearing_initial+360)%360
    return bearing_initial
    
def pitch(lat_sat, long_sat,alt_sat, lat_drone, long_drone,alt_drone):
    R = 6371000
    lat_sat = math.radians(lat_sat)
    lat_drone = math.radians(lat_drone)
    long_sat = math.radians(long_sat)
    long_drone = math.radians(long_drone)
    delta_long = long_drone - long_sat
    delta_lat = lat_drone - lat_sat
    delta_alt = alt_drone-alt_sat
    a = math.pow(math.sin(delta_lat/2),2) + math.cos(lat_sat) * math.cos(lat_drone) * math.pow(math.sin(delta_long/2),2)
    c = 2 * math.atan2(math.sqrt(a),math.sqrt(1-a))
    d = R * c
    pitch_angle = math.atan2(delta_alt,d)
    pitch_angle = math.degrees(pitch_angle)

    return pitch_angle    


def bearingoffset(angle,bearingangleoffset):
    
    newangle = angle +180
    nbearing = bearingangleoffset + 180
    bearing = newangle - nbearing
    
    if newangle > nbearing +180:
        bearing = 360 - bearing
    elif newangle < nbearing -180:
        bearing = 360 - bearign

    if newangle < nbearing :
        bearing = -bearing 
    elif newangle > nbearing +180:
        bearing = - bearing

    return bearing


