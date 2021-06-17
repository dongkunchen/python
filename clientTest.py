import socket
'''
客戶端:創建TCP鏈接時主動發起連接
服務端:接收客戶端的連接
'''

#1.創建一個socket
#參數1: 使定協議 AF_INET 或 AF_INET6
#參數2: SOCK_STREAM執行使用面向流的TCP協議
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#2.建立連接
#參數:是一個元組,第一個為連接的服務器IP地址 第二個端口
sk.connect(("www.sina.com.cn",80))


sk.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

#等待接收數據
data = []
while True:
    #每次接受1K數據
    tempData = sk.recv(1024)
    if tempData:
        data.append(tempData)
    else:
        break
dataStr = (b''.join(data)).decode("utf-8")

#斷開連接
sk.close()
#print(dataStr)

header, HTML = dataStr.split('\r\n\r\n', 1)
print(header)
print(HTML)