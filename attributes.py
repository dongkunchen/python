class Person(object):
    #這裡的屬性實際上屬於類屬性(用類名來調用)
    name = "person"
    def __init__(self, name):
        pass
        #對象屬性(對象調用)
        self.name = name


print(Person.name)
per = Person("tom")
#對象屬性的優先高於類屬性
print(per.name)
#動態的給對象添加對象屬性
per.age = 18#只對當前對象生效,對於類創建的其他對象沒有作用
print(Person.name)
per2 = Person("lilei")
#print(per2.age) per2無age屬性

#刪除對象中的name屬性,再調用會使用同名的類屬性
del per.name
print(per.name)
#注意:以後千萬不要讓對象屬性與類屬性重名
#因為對象屬性會屏蔽類屬型
#當刪除對象屬性後,在使用又會使用類屬性不好掌控