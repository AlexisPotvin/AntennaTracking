import socket



def create_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    return sock


def bind_port(sock, udp_ip, udp_port ):
    sock.bind((udp_ip, udp_port))
    return


def receive_udp_packet(sock):

    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    #print "received message:", data
    return data


