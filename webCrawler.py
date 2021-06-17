import urllib.request

#向指定的url地址發起請求,並返回服務器響應的數據(文件的對象)
response = urllib.request.urlopen("http://www.baidu.com")

#讀取文件的全部內容
data = response.read()
print(data)
#類型
print(type(data))

#將爬取道的網頁寫入文件
with open(r"E:\code\python\day18\file1.html", "wb") as f:
    f.write(data)