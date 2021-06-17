#爬取到直接直接寫入文件
import urllib.request

urllib.request.urlretrieve("http://www.baidu.com", filename=r"E:\code\python\day18\file2.html")

#urlretrieve在執行的過程當中,會產生一些緩存
#清除緩存
urllib.request.urlcleanup()