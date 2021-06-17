class Person(object):

    name = ""
    age = 0
    height = 0
    weight = 0


    def run(self):
        print("run")
    def eat(self, food):
        print("eat" + food)
    def openDoor(self):
        print("我已經打開冰箱門")
    def fillEle(self):
        print("我已經把大象裝進冰箱了")
    def closeDoor(self):
        print("我已經關閉了冰箱門")
'''
實例化對象
格式: 對象名 = 類名(參數列表)
沒有參數,小括號也不能省略

'''

per1 = Person()
print(per1)
print(type(per1))
print(id(per1))

per2 = Person()
print(per2)
print(type(per2))
print(id(per2))