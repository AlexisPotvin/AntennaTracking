import udp
import calcul

UDP_IP = '0.0.0.0'
UDP_PORT = 14555

MAVLINK_MSG_ID_HEARTBEAT = 0
MAVLINK_MSG_ID_GPS_RAW_INT = 24
MAVLINK_MSG_ID_GLOBAL_POSITION_INT = 33

socket = udp.create_socket()

udp.bind_port(socket, UDP_IP, UDP_PORT)
print("bind done")


while 1 :

    data = udp.receive_udp_packet(socket)

    print("hey")
    data_map = map(ord,data)
    hex_data = map(hex,data_map)
    print hex_data, data_map
    payload_lenget = int(hex_data[1],16)


    packet_type = int(hex_data[5],16)

    if packet_type == MAVLINK_MSG_ID_HEARTBEAT :
        if hex_data[0] == '0xfe':

            print "HEART_BEAT"




    elif packet_type == MAVLINK_MSG_ID_GPS_RAW_INT :
        raw_uav_lat = calcul.hex_to_int(hex_data[10:15])
        raw_uav_long = calcul.hex_to_int(hex_data[20:25])
        uav_alt = calcul.hex_to_int(hex_data[25:30])
        uav_lat = raw_uav_lat/10000000
        uav_long = raw_uav_long/10000000
        print "GPS_RAW" "alt" ,uav_alt,"long",uav_long , "alt", uav_alt


    elif packet_type == MAVLINK_MSG_ID_GLOBAL_POSITION_INT :
        print "Global_position"
