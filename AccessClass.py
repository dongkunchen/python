class Person(object):

    name = ""
    age = 0
    height = 0
    weight = 0


    def run(self):
        print("run")
    def eat(self, food):
        print("eat " + food)
    def openDoor(self):
        print("我已經打開冰箱門")
    def fillEle(self):
        print("我已經把大象裝進冰箱了")
    def closeDoor(self):
        print("我已經關閉了冰箱門")

per = Person()

'''
訪問屬性
格式:對象名,屬性名
賦值:對象名,屬性名=新值
'''
per.name = "tom"
per.age = 18
per.height = 160
per.weight = 80
print(per.name,per.age,per.height,per.weight)

'''
訪問方法
格式:對象名.方法名(參數列表)
'''
per.openDoor()
per.fillEle()
per.closeDoor()

per.eat("apple")

#問題:目前來看Person創建的所有對象屬性都是一樣的