from functools import reduce
#python內置了map()和reduce函數()

#map()
#原型 map(fn, lsd)
#參數1是函數
#參數2是序列

#功能:將傳入的函數一次作用在序列中的每一個元素,並把結果做為新的Iterator返回

#將單各字符轉成對應的字面量整數
def char2int(chr):
    return {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}[chr]
list1 = ["2","1","6","5"]

res = map(char2int, list1)
print(res)
print(list(res))
#char2int("2") char2int("1") char2int("6") char2int("5")

#將整數元素的序列,轉為字符串型
#[1,2,3,4] --> ["1","2","3","4"]
l = map(str, [1,2,3,4])
print(list(l))

#reduce(fn, lsd)
#參數1為函數
#參數2為列表
#功能:一個函數作用在序列上,這個函數必須接受兩個參數,reduce把結果繼續和序列的下一個元素累計運算
#reduce(f, [a, b, c, d])
#f(f(f(a, b), c), d)

#求一個序列的和
list2 = [1,2,3,4,5]
#1 + 2
#1 + 2 + 3
#1 + 2 + 3 + 4
#1 + 2 + 3 + 4 + 5
def mySum(x, y):
    return x + y
r = reduce(mySum, list2)
print("r = ", r)

#將字符串轉成對應字面量數字
def str2int(str):
    def fc(x, y):
        return x * 10 +y
    def fs(chr):
        return {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}[chr]
    return reduce(fc, map(fs, list(str)))

a = str2int("12367")
print(a)
print(type(a))

'''
簡單實現自定義Map
def myMap(func, li):
    resList = []
    for parase in li:
        res = func(parase)
    resList.append(res)
'''