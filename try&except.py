'''
try....except...else
格式:
try:
    語句
except 錯誤碼 as e:
    語句2
......
except 錯誤碼 as e:
    語句n
else:
    語句e
注意: else語句可有可無
作用:用來檢驗try語句塊,從而讓except捕獲錯誤信息並處裡

'''

try:
    print(3/0)
except NameError as e:
    print("出現NameError異常")
except ZeroDivisionError as e:
    print("除數為0了")
else:
    print("*********")


try:
    print(4/0)
except:
    print("程序出現異常")

#一次捕獲多個異常
try:
    print(5/0)
except (NameError, ZeroDivisionError):
    print("出現了NameError或ZeroDivisionError錯誤")

#特殊BaseException最大所有異常都能捕獲
try:
    print(5/0)
except BaseException as e:
    print("異常1")
except ZeroDivisionError as e:
    print("異常2")

#跨越多層調用main調用fun2 fun2調用fun1
def func1(num):
    print(1/num)
def func2(num):
    func1(num)
def main():
    func2(0)
try:
    main()
except ZeroDivisionError as e:
    print("******")
'''
try....except...else
格式:
try:
    語句
except 錯誤碼 as e:
    語句2
......
except 錯誤碼 as e:
    語句n
finally:
    語句e

作用:不管有沒有錯誤或有沒有捕獲錯誤都會執行finally

'''
try:
    print(1/0)
except ZeroDivisionError as e:
    print("除0")
finally:
    print("必須執行我")

#斷言assert
def func(num, div):
    assert (div !=0), "div不能為0"
    return num/div

print(func(100,0))