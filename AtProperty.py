class Person(object):
    def __init__(self, name, age):
        self.__age = age
        self.__name = name
    '''
    def getAge(self):
        return self.__age
    def setAge(self, age):
        if age < 0:
            age = 0
        self.__age = age
    '''
    #方法名為受限制的變量去掉雙下滑線
    @property
    def age(self):
        return self.__age
    @age.setter #去掉下滑線.setter
    def age(self, age):
        if age < 0:
            age = 0
        self.__age = age

    @property
    def name(self):
        return self.__name
    @name.setter  # 去掉下滑線.setter
    def name(self, name):
        self.__name = name

per = Person("tom", 18)

#屬性直接對外暴露
#不安全,沒有數據的過濾
#per.age = -10
#print(per.age)

#使用限制訪問,需要自己寫set和get方法才能訪問
#per.setAge(15)
#print(per.getAge())

per.age = 100 #相當於調用setAge方法
print(per.age) #相當於調用getAge方法

print(per.name)
#property:可以讓你對受限制訪問的屬性使用點方法