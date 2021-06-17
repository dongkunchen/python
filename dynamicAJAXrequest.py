import json
import urllib.request
import ssl

def ajaxCrawler(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Mobile Safari/537.36"
    }
    req = urllib.request.Request(url, headers=headers)

    #使用ssl創建未驗證的上下文
    context = ssl._create_unverified_context()

    response = urllib.request.urlopen(req,context=context)
    jsonStr = response.read().decode("utf-8")
    jsonData = json.loads(jsonStr)
    return jsonData
'''
url = "https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0"
info = ajaxCrawler(url)
print(info)
'''
for i in (1, 11):
    url = "https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start="+str(i*20)
    info = ajaxCrawler(url)
    print(len(info))