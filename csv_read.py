import csv

def readCsv(path):
    infoList = []
    with open(path,"r") as f:
        allFileInfo = csv.reader(f)
        print(allFileInfo)
        for row in allFileInfo:
            infoList.append(row)
    return infoList
path = r"E:\code\python\000002.csv" #完整路徑+檔名
info = readCsv(path)
# for row in info:
#     print(row)