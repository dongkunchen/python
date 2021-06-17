'''
給你一串字符串判斷是否為手機號

'''

def checkPhone(str):
    if len(str) != 10:
        return False
    elif str[0] != "0":
        return False
    elif str[1:2] != "9":
    #elif str[1:2] != "9" and str[1:2] != "9":
        return False
    for i in str:
        if i < "0" or i > "9":
            return False
    return True

print(checkPhone("09331111111"))
print(checkPhone("0933111111"))
print(checkPhone("19331111111"))
print(checkPhone("1233112111"))
print(checkPhone("09331a1111"))
