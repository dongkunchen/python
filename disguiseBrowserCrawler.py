import urllib.request
import random

url = "http://www.baidu.com"

'''
#模擬請求頭
headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Mobile Safari/537.36"
}
#設置一個請求體
req = urllib.request.Request(url,headers=headers)

#發起請求
response = urllib.request.urlopen(req)
data = response.read().decode("utf-8")
print(data)
'''

agentsList = [
    "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Mobile Safari/537.36"
]
agentStr = random.choice(agentsList)
req = urllib.request.Request(url)
#向請求體裡添加了user-agent
req.add_header("user-agent", agentStr)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
