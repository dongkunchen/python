import itertools
'''
排列組合
'''
mylist = list(itertools.product("0123456789abcd", repeat=10))
print(mylist)
print(len(mylist))