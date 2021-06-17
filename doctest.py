import doctest

#文檔測試
#doctest模塊可以提取註釋中的代碼執行
#doctest嚴格按照python交互模式的輸入提取
def mySum(x, y):
    '''
    get the Sum from x and y
    :param x:firstNum
    :param y:secondNum
    :return:sum

    example:
    >>> print(mySum(1,2))
    3
    '''
    return x + y


print(mySum(1,2))

#進行文檔測試
doctest.testmod()