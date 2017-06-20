
import socket

UDP_IP_ADDRESS = '192.168.1.68'
UDP_PORT_NO = 8896

listeningSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

listeningSock.bind((UDP_IP_ADDRESS,UDP_PORT_NO))

print('Created UDP socket on {0} with port {1}.'.format(UDP_IP_ADDRESS,UDP_PORT_NO))
print('Now listening for messages...\n\n')

while True:
	data, addr = listeningSock.recvfrom(1024)

	print(data)