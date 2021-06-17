'''
概念:一種保存數據的格式
作用:可以保存本地的JSON文件,也可以將JSON串進行傳輸,
通常將JSON稱為輕量級的傳輸

{} 代表對象(字典)
[] 代表列表
: 代表鍵值對
, 分隔兩部分
'''
import json

jsonStr = '{"name":"sunck凱","age":18,"hobby":["money","power","english"],"parames":{"a":1,"b":2}}'

#將json格式的字符串轉成python的數據類型的對象
jsonData = json.loads(jsonStr)
print(jsonData)
print(jsonData["hobby"])

#將python 轉json
jsonData2 = {"name":"sunck凱","age":18,"hobby":["money","power","english"],"parames":{"a":1,"b":2}}
jsonStr2 = json.dumps(jsonData2)
print(jsonStr2)
print(type(jsonStr2))

#讀取本地的json文件
path1 = r"E:\code\python\1.json"
with open(path1, "rb") as f:
    data = json.load(f)
    print(data)
    #字典類型
    print(type(data))

#寫本地json
path2 = r"E:\code\python\a.json"
jsonData3 = {"name":"sunck凱","age":18,"hobby":["money","power","english"],"parames":{"a":1,"b":2}}
with open(path2, "w") as f:
    json.dump(jsonData3, f)