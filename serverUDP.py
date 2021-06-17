import socket

udpServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpServer.bind(('192.168.0.100',8080))

while True:
    data, addr = udpServer.recvfrom(1024)
    print("客戶端說: ", data.decode("utf-8"))
