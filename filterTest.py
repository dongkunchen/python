'''
原型:filter(fn, lsd)
參數1為函數
參數2為序列

功能:用於過濾序列
白話文:把傳入的函數依次作用與序列每個元素,根據返回的是ture false判斷是否保留

'''
list1 = [1,2,3,4,5,6,7,8,9]
#篩選條件
def func(num):
    #偶數保留
    if num%2 == 0:
        return True
    #奇數剃除
    return False
l = filter(func, list1)

print(list(l))

data = [["姓名","年齡","愛好"],["tom", 25, "打球"],["alice", 26, "金錢"]]

def func2(v):
    v = str(v)
    if v == "打球":
        return False
    return True
for line in data:
    m = filter(func2, line)
    print(list(m))