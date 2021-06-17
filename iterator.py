from collections import Iterable
from collections import Iterator
'''
可迭代對象:可以直接作用於for循環的對象統稱為可迭代對象
(Iterable)可以用isinstance()去判斷一個對象是否是Iterable對象

可以直接作用於for的數據類型一般分兩種
1.集合數據類型如list tuple dict set string
2.是generator 包括生成器和帶yield的generator function

'''
print(isinstance([], Iterable))
print(isinstance((), Iterable))
print(isinstance({}, Iterable))
print(isinstance("", Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(1, Iterable))

'''
迭代器:不但可以作用於for循環,還可以被next()函數不斷調用並返回下一個值
直到最後會拋出一個StopIteration錯誤表示無法繼續返回下一個值

可以被next()函數調用並不斷返回下一個值的對象稱為迭代器
(Iterator對象)

可以使用isinstance()函數判斷一個對象是否是Iterator對象

'''
print(isinstance([], Iterator))
print(isinstance((), Iterator))
print(isinstance({}, Iterator))
print(isinstance("", Iterator))
print(isinstance((x for x in range(10)), Iterator))

l = (x for x in range(5))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
#print(next(l))報錯

#轉成Iterator對象
a = iter([1,2,3,4,5])
print(next(a))
print(next(a))
print(isinstance(iter([]), Iterator))
print(isinstance(iter(()), Iterator))
print(isinstance(iter({}), Iterator))
print(isinstance(iter(""), Iterator))



