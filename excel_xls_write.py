#有序字典
from collections import OrderedDict

#寫入數據只能寫xls
from pyexcel_xls import save_data

def makeExcelFile(path, data):
    dic = OrderedDict()
    for sheetName, sheetValue in data.items():
        d = {}
        d[sheetName] = sheetValue
        dic.update(d)
    save_data(path, dic)

path = r"E:\code\python\b.xls"
makeExcelFile(path, {"表一":[[1,2,3],[4,5,6],[7,8,9]],"表二":[[11,22,33],[44,55,66],[77,88,99]]})