import math



def bearing(lat1,lon1,lat2,lon2):

    dlat = lat2 - lat1
    dlon = lon2 - lon1
    y = math.sin(lon2-lon1)*math.cos(lat2)
    x = math.cos(lat1)*math.sin(lat2)-math.sin(lat1)*math.cos(lat2)*(math.cos(lon2-lon1))
    if y > 0:
        if x > 0:
            tc1 = math.degrees(math.atan(y/x))
        if x < 0:
            tc1 = 180 - math.degrees(math.atan(-y/x))
        if x == 0:
            tc1 = 90
    if y < 0:

        if x > 0:
            tc1 = -math.degrees(math.atan(-y/x))
        if x < 0:
            tc1 = math.degrees(math.atan(y/x))-180
        if x == 0:
            tc1 = 270
    if y == 0:
        if x > 0:
            tc1 = 0
        if x < 0:
            tc1 = 180
        if x == 0:
            tc1 = 0

    return tc1


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


