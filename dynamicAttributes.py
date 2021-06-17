from types import MethodType
#創建一個空類

class Person(object):
    __slots__ = ("name", "age", "speak")


per = Person()
#動態添加屬性,這體現了動態語言的特點(靈活)
per.name = "tom"
print(per.name)
#動態添加方法
'''
def say(self):
    print("my name is " + self.name)
per.speak = say
per.speak()#無法調用等於沒添加
'''
#1.先from types import MethodType

#2.定義方法
def say(self):
    print("my name is " + self.name)
#3.添加方法
per.speak = MethodType(say, per)
#4.調用動態添加進去的方法
per.speak()

#思考:如果我們想要限制實例的屬性怎麼辦?
#比如只允許給對象添加name,age,height,weight屬性
#解決:定義類的時候,定義一個特殊的屬性(__slots__)可以限制動態添加的屬性

per.height = 172
print(per.height)