'''
TCP建立可靠的連接,並通信雙方都可以都可以已流的形式發送數據
相對於TCP UDP是面相無連接的協議

使用UDP協議時不需要建立連接只需要知道對方IP跟端口
就可以直接發送數據包 但是能不能倒打就不知道了

雖然UDP傳輸數據不可靠但他優點比TCP速度快對於要求不高的數據可以用UDP
'''
import socket
import time

str = "dongkun is a handsome man"
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.connect(("192.168.0.100", 8080))
udp.send(str.encode("utf-8"))
'''
while True:
    udp.send("dongkun is a handsome man".encode("utf-8"))
    time.sleep(1)
'''