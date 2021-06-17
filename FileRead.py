'''
過程:
1.打開文件
2.讀取文件內容
3.關閉文件
'''

'''
1.打開文件
open(path,flag)
path:要打開文件的路徑
flag:打開方式
r 以只讀方式打開,文件的描述符放在文件的開頭
rb 以二進制格式打開一個文件用於只讀,文件的描述符放在文件的開頭
r+ 打開一個文件用於讀寫,文件的描述符放在文件的開頭
w  打開一個文件只用於寫入,以存在覆蓋,未存在創建
wb 打開一個文件用二進制寫入,以存在覆蓋,未存在創建
w+ 打開一個文件用於讀寫
a  打開文件用於追加,如果文件存在則文件的描述符放在文件的末尾
a+
encoding:編碼方式
errors:錯誤處理
'''

'''
打開
'''
path = "file.txt"
#f = open(path,"r",encoding="utf-8",errors)
f = open(path,"r")

'''
讀文件內容
'''
#1.讀取文件全部內容
# str1 = f.read()
# print(str1)

#2.只讀取指定字符數
# str2 = f.read(10)
# print("*"+str2+"*")

#3.讀取整行,包括"\n"字符
# str4 = f.readline()
# print(str4)
# str5 = f.readline()
# print(str5)

#4.讀取指定字符數
# str6 =f.readline(10)
# print(str6)

#5.讀取所有行並返回列表
# list7 = f.readlines()
# print(list7)

#6.若給定的數字大於0,返回實際大小的字節的整行
# list8 = f.readlines(22)
# print(list8)

#seek修改描述符的位置
f.seek(10)
str9 = f.read()
print(str9)

'''
關閉文件
'''
f.close()

#一個完整的過程
try:
    f1 = open(path, "r", encoding="utf-8")
    print(f1.read())
finally:
    if f1:
        f1.close()

#方式二
with open(path, "r", encoding="utf-8") as f2:
    print(f2.read())