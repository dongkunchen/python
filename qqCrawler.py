import urllib.request
import ssl
import re
import os

def writeFileBytes(htmlBytes, toPath):
    with open(toPath, "wb") as f:
        f.write(htmlBytes)
def writeFileStr(htmlBytes, toPath):
    with open(toPath, "w") as f:
        f.write(str(htmlBytes))

def getHtmlBytes(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
    }
    req = urllib.request.Request(url, headers=headers)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req,context=context)
    return response.read()

def qqCrawler(url, toPath):
    htmlBytes = getHtmlBytes(url)
    # writeFileBytes(htmlBytes,r"E:\code\python\images\File1.txt")
    # writeFileStr(htmlBytes,r"E:\code\python\images\File2.txt")
    htmlStr = str(htmlBytes)
    pat = r"[1-9]\d{4,9}"
    re_qq = re.compile(pat)
    qqsList = re_qq.findall(htmlStr)
    #去重
    qqsList = list(set(qqsList))
    print(qqsList)
    print(len(qqsList))


url = "https://tieba.baidu.com/p/421767762?red_tag=0556308855"
toPath = r"E:\code\python\images\qqFile.txt"
qqCrawler(url, toPath)