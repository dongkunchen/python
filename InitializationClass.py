class Person(object):

    # name = ""
    # age = 0
    # height = 0
    # weight = 0


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


'''
構造函數:__init__() 在使用類創建對象自動調用
注意:如果不創建默認自動添加一個空的
'''

per = Person("dongkun",20,170,55)
print(per.name,per.age)
per1 = Person("dongkun1",22,160,75)
print(per1.name,per1.age)