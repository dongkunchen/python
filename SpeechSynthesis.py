#語音合成
#系統客戶端
import time

import win32com.client
dehua = win32com.client.Dispatch("SAPI.SPVOICE")
dehua.Speak("sunck is a good man")

while 1:
    dehua.Speak("sunck is a good man")
    time.sleep(5)