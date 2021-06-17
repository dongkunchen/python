'''
單元測試:

作用:用來對一個函數,一個類或是一個模塊來進行正確性校驗工作

結果:
1.單元測試通過,說明我們測試的函數功能正常
2.單元測試不通過,說明函數功能有BUG,要嘛測試條件輸入有誤

'''

def mySum(x, y):
    return x + y

def mySub(x, y):
    return x - y

print(mySum(1,2))