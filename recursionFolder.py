import os
import collections
#遞歸遍歷當前目錄
# def getAllDir(path):
#     fileList = os.listdir(path)
#     print(fileList)
# getAllDir(r"E:\code")

def getAllDir(path):
    #得到當前目錄所有的文件
    fileList = os.listdir(path)
    #處理每一個文件
    for fileName in fileList:
        #判斷是否是路徑(要用絕對路徑)
        fileAbsPath = os.path.join(path,fileName)
        if os.path.isdir(fileAbsPath):
            print("目錄:",fileName)
            getAllDir(fileAbsPath)
        else:
            print("普通文件:",fileName)
getAllDir(r"E:\code")

#遍歷當前目錄下所有目錄(深度變歷)先進後出
# def getAllDirDE(path):
#     stack = []
#     stack.append(path)
#     #處理棧,當棧為空的時候結束循環
#     while len(stack) != 0:
#         dirPath = stack.pop()
#         filesList = os.listdir(dirPath)
#         #處理每一個問價,如果是普通文件則打印出來,如果是目錄則將目錄地址壓棧
#         for fileName in filesList:
#             fileAbsPath = os.path.join(dirPath,fileName)
#             if os.path.isdir(fileAbsPath):
#                 #是目錄就押棧
#                 print("目錄: " + fileName)
#                 stack.append(fileAbsPath)
#             else:
#                 #打印普通文件
#                 print("普通: " + fileName)
# getAllDirDE(r"E:\code")

#列隊模擬遞歸變歷目錄(廣度遍歷)先進先出

def getAllDirQU(path):
    queue = collections.deque()
    #進隊
    queue.append(path)
    while len(queue) != 0:
        #出隊數據
        dirPath = queue.popleft()
        #找出所有文件
        filesList = os.listdir(dirPath)
        for fileName in filesList:
            #絕對路徑
            fileAbsPath = os.path.join(dirPath, fileName)
            #判斷是否是目錄,是目錄就近隊,不是就打印
            if os.path.isdir(fileAbsPath):
                print("目錄: " + fileName)
                queue.append(fileAbsPath)
            else:
                print("普通文件: " + fileName)
getAllDirQU(r"E:\code")