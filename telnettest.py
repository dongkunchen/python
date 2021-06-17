import telnetlib

def telnetDoSomething(IP, user, password, command):
   try:
       # 連接服務器
       telnet = telnetlib.Telnet(IP)
       # 設置調適級別
       telnet.set_debuglevel(2)
       # 讀取輸入用戶名信息
       rt = telnet.read_until("Login username:".encode("utf-8"))
       # 寫入用戶名
       telnet.write((user + "\r\n").encode("utf-8"))
       # 讀取輸入密碼信息
       rt = telnet.read_until("Domain name:".encode("utf-8"))
       # 寫入用戶密碼
       telnet.write((password + "\r\n").encode("utf-8"))
       # 讀取驗證IP
       rt = telnet.read_until("Domain name:".encode("utf-8"))
       # 寫入用戶名
       telnet.write((IP + "\r\n").encode("utf-8"))

       # 登錄成功,寫指令
       rt = telnet.read_until(">".encode("utf-8"))
       telnet.write((command + "\r\n").encode("utf-8"))

       # 上面命令執行成功會繼續讀到尖括號
       # 失敗,一般不會是尖括號
       rt = telnet.read_until(">".encode("utf-8"))

       # 斷開連接
       telnet.close()
       return True
   except:
       return False

if __name__ == "__main__":
    IP = "192.168.119.128"
    user =
    password =
    command =
    telnetDoSomething(IP, user, password, command)