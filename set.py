'''
set:類似dict,是一組key的集合,不存儲value
本質:無序和無重複元素的集合
'''

#創建
#創建set需要一個list或者tuple或者dict作為輸入集合
#重複元素在set中會自動被過濾
s1 = set([1,2,3,4,5,3,4,5])
print(s1)
s2 = set((1,2,3,3,2,1))
print(s2)
s3 = set({1:"good",2:"nice"})
print(s3)

#添加
s4 = set([1,2,3,4,5])
s4.add(6)
s4.add(3)#可以添加無效果
#s4.add([7,8,9]) 抱錯 set的元素不能list因為可變
s4.add((7,8,9))#元組可以因為不可變
#s4.add({1:"a"}) 因為字典可變
print(s4)

#插入(類似拼接)
s5 = set([1,2,3,4,5])
s5.update([6,7,8])
s5.update((9,10))
s5.update("sunck")
print(s5)

#刪除
s6 = set([1,2,3,4,5])
s6.remove(3)
print(s6)

#遍歷
s7 = set([1,2,3,4,5])
for i in s7:
    print(i)
#set沒有索引的
#print(s7[3])
for index, data in enumerate(s7):
    print(index, data)

s8 = set([1,2,3])
s9 = set([2,3,4])
#交集
a1 = s8 & s9
print(a1)
print(type(a1))
#並集
a2 = s8 | s9
print(a2)
print(type(a2))