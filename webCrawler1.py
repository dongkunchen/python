import urllib.request

#向指定的url地址發起請求,並返回服務器響應的數據(文件的對象)
response = urllib.request.urlopen("http://www.baidu.com")

#讀取文件的全部內容
# data = response.read()
# print(data)
# #類型
# print(type(data))
#讀取一行
#data = response.readline()

#讀取文件的全部內容,會把讀取到的數據賦值給一個列表變量
data = response.readlines()
'''
print(data)
print(type(data))
print(len(data))
print(type(data[100].decode("utf-8")))
'''
#將爬取道的網頁寫入文件
# with open(r"E:\code\python\day18\file1.html", "wb") as f:
#     f.write(data)

#response屬性
#返回當前環境的有關信息
print(response.info())

#返回狀態碼
print(response.getcode())
#if response.getcode() == 200 or response.getcode == 304:
    #處裡網頁信息
#    pass

#返回當前正在爬取的URL地址
print(response.geturl())



url = r"https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%87%B1%E5%93%A5&fenlei=256&rsv_pq=9fb9ec9f0008f300&rsv_t=eff5jnUB8nkzs8pSGLxpr2FI95rG1oZe2msFENarACUuXP8z%2FBryzRhkZwo&rqlang=cn&rsv_dl=tb&rsv_enter=1&rsv_sug3=12&rsv_sug1=6&rsv_sug7=101&rsv_sug2=0&rsv_btype=i&inputT=5666&rsv_sug4=5666"
#解碼
newUrl1 = urllib.request.unquote(url)
print(newUrl1)
#編碼
newUrl2 = urllib.request.quote(newUrl1)
print(newUrl2)