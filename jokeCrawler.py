import urllib.request
import re

def jokeCrawler(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
    }
    req = urllib.request.Request(url, headers=headers)
    respone = urllib.request.urlopen(req)
    HTML = respone.read().decode("utf-8")

    pat = r'<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">'
    re_joke = re.compile(pat, re.S)
    divsList = re_joke.findall(HTML)
    # print(divsList)
    # print(len(divsList))
    dic = {}
    for div in divsList:
        #用戶名
        re_u = re.compile(r"<h2>(.*?)</h2>", re.S)
        username = re_u.findall(div)
        username = username[0]
        #段子
        re_d = re.compile(r'<div class="content">\n<span>(.*?)</span>', re.S)
        duanzi = re_d.findall(div)
        duanzi = duanzi[0]


        dic[username] = duanzi

    return dic

    # with open(r"E:\code\python\day18\file3.html", "wb") as f:
    #     f.write(HTML)


url = "https://www.qiushibaike.com/text/page/1/"
info = jokeCrawler(url)

for k,v in info.items():
    print(k + "說\n" + v)