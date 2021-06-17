'''
特點:把數據拼接到請求路徑的後面傳遞給服務器
優點:速度快
缺點:承載的數據量小,不安全
'''
import urllib.request
url = ""
response = urllib.request.urlopen(url)
data = response.read().decode("utf-8")
print(data)
print(type(data))