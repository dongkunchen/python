import socket

#創建一個socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#綁定IP端口
server.bind(('192.168.0.100',8080))
#監聽
server.listen(5)
#等待連接
clientSocket, clientAddress = server.accept()

while True:
    data = clientSocket.recv(1024)
    print("客戶端說: " + data.decode("utf-8"))#收到客戶端數據
    sendData = input(("輸入返回給客戶端的數據"))
    clientSocket.send(sendData.encode("utf-8"))