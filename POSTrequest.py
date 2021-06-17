'''
特點:把參數進行打包 單獨傳輸
優點:數量大 安全(當對服務器數據進行修改時建議使用POST)
缺點:速度慢
'''
import urllib.request
import urllib.parse

url = ""
#將要發送的數據合成一個字典
#字典的鍵去網址裡找,一般為input標籤的name屬性的值
data = {
    "username":"sunck",
    "passwd":"666"
}
#對要發送的數據進行打包
postData = urllib.parse.urlencode(data)
#請求體
req = urllib.request.Request(url, postData)
#請求
req.add_header("user-agent", "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Mobile Safari/537.36")
response = urllib.request.urlopen(req)
print(response.data().decode("utf-8"))
