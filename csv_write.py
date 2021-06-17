import csv

def writeCsv(path, data):
    with open(path, "w") as f:
        writer = csv.writer(f)
        for rowData in data:
            writer.writerow(rowData)

path = r"E:\code\python\000002.csv" #寫入完整路徑 +檔名

writeCsv(path, [[1,2,3],[4,5,6],[7,8,9]])