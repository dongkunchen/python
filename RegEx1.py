import re
#pip 包管理工具
'''
python 1.5以後出現re模塊
re模塊使python語言擁有了全部正則表達式功能

re.match函數
原型:match(pattern, string, flags=0)
pattern:匹配的政則表達式
string:要匹配的字符串
flags:標誌位,用於控制正則表達式的匹配方式,值如下
re.I 忽略大小寫
re.L 做本地戶識別
re.M 多行匹配,影響^和$
re.S 是.匹配包括換行符在內的所有字符
re.U 根據Unicode字符集解析字符,影響\w \W \b \B
re.X 使我們以更靈活的格式理解正則表達式
參數:
功能:嘗試從字符串的起始位置匹配一個模式,如果不是起始位置匹配成功的話返回None
'''
#www.yahoo.com
print(re.match("www","www.yahoo.com"))#匹配
print(re.match("www","www.yahoo.com").span())#單獨取位置
print(re.match("www","ww.yahoo.com"))#none
print(re.match("www","yahoo.wwwcom"))#none
print(re.match("www","wwW.yahoo.com"))#none
print(re.match("www","wwW.yahoo.com", flags=re.I))#匹配
#掃描整個字符串,返回從起始位置成功的配置
print("******************************")
'''
re.search
原型:search(pattern, string, flage=0)
pattern:匹配的政則表達式
string:要匹配的字符串
flags:標誌位,用於控制正則表達式的匹配方式
功能:掃描整個字符串,並返回第一個成功的匹配
'''
print(re.search("dongkun","handsome man is dongkun!dongkun is a cool man"))
print("******************************")
'''
re.findall函數
原型:findall(pattern, string, flage=0)
pattern:匹配的政則表達式
string:要匹配的字符串
flags:標誌位,用於控制正則表達式的匹配方式
功能:掃描整個字符串,並返回結果列表
'''
print(re.findall("dongkun","handsome man is dongkun!Dongkun is a cool man", flags=re.I))