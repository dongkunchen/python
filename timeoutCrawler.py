import urllib.request

#如果網頁長時間未響應,系統判斷超時,無法爬取
for i in range(1, 100):
    try:
        respone = urllib.request.urlopen("http://www.baidu.com", timeout=0.5)
        print(len(respone.read().decode("utf-8")))
    except:
        print("請求超時,繼續下一個爬取")