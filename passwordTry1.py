import itertools
'''
破解密碼
排列
'''

mylist = list(itertools.permutations([1,2,3,4], 3))
print(mylist)
print(len(mylist))

'''
前提沒重複...沒驗證碼
'''