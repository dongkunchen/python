import socket, sys
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('192.168.0.100', 8080))


def send_msg():
    while True:
        msg = input('請輸入您要發送的內容:')
        s.sendto(msg.encode('utf8'),('192.168.0.100', 9090))
        if msg == 'exit':
            break
def recv_msg():

    while True:
        data, addr = s.recvfrom(1024)
        print('接收到了{}地址{}端口的消息:{}'.format(addr[0], addr[1], data.decode('utf8')),file = open('messagelog.txt', 'a', encoding='utf8'))

t1 = threading.Thread(target=send_msg)
t2 = threading.Thread(target=recv_msg)

t1.start()
t2.start()