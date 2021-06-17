import requests
import re
import time
import os
import random
baseurl= "https://www.vmgirls.com/15400.html"
headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Mobile Safari/537.36"
}
#自己的身份
response = requests.get(baseurl,headers=headers)
# print(response.request.headers)
# print(response.text)
html = response.text
"""解析網頁"""
urls = re.findall('alt="" data-pagespeed-lsc-url="(.*?)" /></a>',html)
# print(urls)
dir_name = re.findall('<title>(.*?)</title>',html)
print(type(dir_name))
print(dir_name)
dir_name = str(dir_name)
print(type(dir_name))
print(dir_name)
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
"""保存圖片"""
print(urls)
for url in urls:
    time.sleep(2)
    photo_name = url.split('/')#保存圖片的名字
    print(photo_name)
    photo = requests.get(url,headers=headers)
    with open(dir_name+"/"+photo_name,"wb") as file:
         file.write(photo.content)