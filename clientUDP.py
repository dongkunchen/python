import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = input("請輸入數據")
    client.sendto(data.encode("utf-8"), ('192.168.0.100',8080))
