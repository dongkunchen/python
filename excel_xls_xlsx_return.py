#有序字典
from collections import OrderedDict

#讀取數據
from pyexcel_xls import get_data

def readXlsAndXlsxFile(path):
    dic = OrderedDict()

    #抓取數據
    xdata = get_data(path)

    for sheet in xdata:
        dic[sheet] = xdata[sheet]
    return dic
path = r"E:\code\python\1.xlsx"
dic = readXlsAndXlsxFile(path)
print(dic)
print(len(dic))