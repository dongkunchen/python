#排序: 冒泡 選擇      快速 插入 計數器

#普通排序
list1 = [4,7,2,6,3]
list2 = sorted(list1)#默認升序
print(list1)
print(list2)

# #案絕對值大小排序
list3 = [4,-7,2,6,-3]
# #key接受函數來實現自定義排序規則
list4 = sorted(list3, key=abs)#默認升序
print(list3)
print(list4)

#降序
list5 = [4,7,2,6,3]
list6 = sorted(list5, reverse=True)#默認升序reverse反轉
print(list5)
print(list6)

#函數自己寫按長度沒key按碼
def myLen(str):
    return len(str)
list7 = ['b33','a33333','c333','d333333']
list8 = sorted(list7, key=mylen)#默認升序
print(list7)
print(list8)
