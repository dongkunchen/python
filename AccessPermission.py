class Person(object):
    def run(self):
        print("run")
    def eat(self, food):
        print("eat " + food)
    def __init__(self,name,age,height,weight,money):
        #print(name,age,height,weight)
        self.name = name
        self.__age__ = age
        self._height = height
        self.weight = weight
        self.__money = money#如果要讓內部屬性不被外部直接訪問加兩個__
    def setMoney(self,money):#內部取用
        if money < 0:
            money = 0
        self.__money = money
    def getMoney(self):
        return self.__money

per = Person("dongkun", 20, 182, 62, 300000000)
per.age = 10
print(per.age)
#外部不能使用內部可以使用但是動態可以賦值

print(per.getMoney())
#不能直接訪問per.__money是因為python解釋成_Person__money
#python本質上只是改名字達成私有
#可以用_Person__money訪問但不建議使用,版本不同名字不同


#在python中__XXX__屬於特殊屬性並非私有化也能直接訪問
print(per.__age__)

#python中 _XXX 變量外部可以訪問但是請幫我視為私有
print(per._height)