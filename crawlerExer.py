import urllib.request
import re
import os
import ssl


def imageCrawler(url, toPath):

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
    }
    req = urllib.request.Request(url, headers=headers)

    context = ssl._create_unverified_context()

    response = urllib.request.urlopen(req,context=context)
    HtmlStr = response.read().decode("utf-8")
    # with open(r"E:\code\python\images\f1.html", "wb") as f:
    #     f.write(HtmlStr)
    pat = r'<img width="220" height="220" data-img="1" data-lazy-img="done" source-data-lazy-img src="//(.*?)">'
    re_image = re.compile(pat, re.S)
    imagesList = re_image.findall(HtmlStr)
    num = 1
    for imageUrl in imagesList:
        path = os.path.join(toPath, str(num)+".jpg")
        num += 1
        #把圖片下載到本地存儲
        urllib.request.urlretrieve("http://"+imageUrl,filename=toPath)

url = "https://list.jd.com/list.html?cat=1315,1343,9719&page=1&delivery_glb=1&sort=sort_rank_asc&trans=1&JL=4_16_0#J_main"
toPath = r"E:\code\python\images"
