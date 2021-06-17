path = "file.txt"
f = open(path,"w")

#寫文件
#1.將信息寫入緩衝區
f.write("good man")
#2.刷新緩衝區
#直接把內部緩衝區立即寫入不用等close
f.flush()



f.close()

with open(path,"a") as f2:
    f2.write("nick man")

#編碼
path = "file1.txt"
with open(path,"wb") as f3:
    str = "sunck is a good man"
    f3.write(str.encode("utf-8"))

with open(path,"rb") as f4:
    data = f4.read()
    print(data)
    print(type(data))
    newData = data.decode("utf-8")
    print(newData)
    print(type(newData))