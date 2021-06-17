import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.0.100',8080))

while True:
    data = input("請輸入給服務器發送的數據")
    client.send(data.encode("utf-8"))#給服務端發數據
    info = client.recv(1024)
    print("服務器說: ", info.decode("utf-8"))#收到服務端數據


