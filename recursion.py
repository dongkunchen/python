'''
遞歸調用:一個函數,調用了自身,稱為遞歸調用
遞歸函數:一個會調用自身的函數稱為遞歸函數
凡是循環能做的事,遞歸都能做
'''
'''
方式:
1.寫出臨界條件
2.找這一次和上一次的關係
3.假設當前函數已經能用,調用自身計算上一次的結果,在求出本次的結果
'''

#輸入一個數(大於等於1),求1+2+3+...+n的和
# def sum1(n):
#     sum = 0
#     for x in range(1, n + 1):
#         sum += x
#     return sum
# res = sum1(5)
# print("res =", res)

#遞歸寫
'''
1+2+3+4+5
'''
def sum2(n):
    if n == 1:
        return 1
    else:
        return n + sum2(n - 1)
res = sum2(5)
print("res =", res)