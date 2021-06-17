'''
析構函數:__del__() 釋放對象時自動調用
'''


class Person(object):


    def run(self):
        print("run")
    def eat(self, food):
        print("eat " + food)
    def __init__(self,name,age,height,weight):
        #print(name,age,height,weight)
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def __del__(self):
        print("這裡是析構函數")

per = Person("tom", 20, 170, 55)
#釋放對象
del per
#釋放之後不能在訪問

#在函數裡定義的對象,會在函數結束時自動釋放
#減少內存空間浪費
def func():
    per2 =  Person("aa", 120, 200, 50)
func()