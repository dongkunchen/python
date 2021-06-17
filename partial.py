import functools

print (int("1010", base = 2))
#自定義偏函數
def int2(str, base = 2):
    return int(str,base)
print(int2("1011"))

#用模塊形成一個新的函數
int3 = functools.partial(int, base = 2)
print(int3("1011"))