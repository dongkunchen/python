#發郵件的庫
import smtplib
#郵件文本
from email.mime.text import MIMEText

#SMTP服務器

#發郵件的地址
sender = "etu0644@gmail.com"
#發送者郵箱的密碼
passwd = "a84458204"
#轉換成郵件文本
msg = MIMEText("content")
#標題
msg["Subject"] = "good man"
#發送者
msg["From"] = sender
#
msg["to"] = "etu064@yahoo.com.tw"

#創建SMTP服務器
mailServer = smtplib.SMTP_SSL("smtp.gmail.com", 465)
mailServer.ehlo()
mailServer.starttls()
#登陸郵箱
mailServer.login(sender, passwd)
mailServer.send_message(msg)
#退出郵箱
mailServer.quit()