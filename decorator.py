'''
概念:是一個閉包把一個函數當作參數返回值替代版的函數
本質上就是一個返回函數的函數
'''

# #簡單的裝飾器
# def func1():
#     print("sunck is a good man")
#
# def outer(func):
#     def inner():
#         print("*************")
#         func()
#     return inner
# #f是函數func1的加強版本
# f = outer(func1)
# f()

#複雜一點的裝飾器
# def outer(func):
#     def inner(age):
#         if age < 0:
#             age =0
#         func(age)
#     return inner
# #使用@符號將裝飾器應用到函數
# @outer#相當於say = outer(say)
# def say(age):
#     print("sunck is %d years old" % (age))
#
# say(-10)

#通用裝飾器
def outer(func):
    def inner(*args, **kwargs):
        #添加修改的功能
        print("&&&&&&&")
        func(*args, **kwargs)
    return inner
@outer
def say(name, age):
    print("my name is %s, I am %d years"%(name, age))

say("sunck", 18)