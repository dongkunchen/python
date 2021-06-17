import pickle

#寫
myList = [1,2,3,4,5,"sunck is a good man"]
path = r"file.txt"
f = open(path,"wb")
pickle.dump(myList,f)
f.close()

#讀
f1 = open(path,"rb")
tempList = pickle.load(f1)
print(tempList)
f1.close()