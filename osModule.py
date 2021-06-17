import os

'''
os:包含了普遍的操作系統的功能

'''
#獲取操作系統類型 nt-->window posix-->Linux,Unix或 Mac OS X
print(os.name)

#打印詳細內容window不支持
#print(os.uname())

#獲取操作系統的環境變量
print(os.environ)

#獲取指定環境變量
#print(os.environ.get("ALLUSERSPROFILE"))

#獲取當前目錄
print(os.curdir)

#獲取當前工作目錄,即當前python腳本所在的目錄
print(os.getcwd())

#以列表的形式返回指定目錄下的所有文件
print(os.listdir(r"E:\code"))

#在當前目錄下創建新目錄
#os.mkdir("dongkun")

#刪除目錄
#os.rmdir("sunck")

#獲取文件屬性
#print(os.stat("sunck"))

#重命名
#os.rename("sunck","kaige")

#刪除普通文件
#os.remove("file.txt")

#運行shell命令
#os.system("notepad")
#os.system("msconfig")

#有些方法存在os模塊裡還有些存在os.path
#查看當前的絕對路徑
#os.path.abspath("./kaige")
#拼接路徑
# p1 = r"C:\Users\"
# p2 = r"cunck\abc\d"
# #注意參數2裡開始不要有斜槓
# print(os.path.join(p1,p2))