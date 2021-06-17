'''
self代表類的實例,而非類
那個對象調用方法,那麼該方法中的self就代表那個對象
self__class__ 代表類名_

'''
class Person(object):

    # name = ""
    # age = 0
    # height = 0
    # weight = 0


    def run(self):
        print("run")
        print(self.__class__)
        p = self.__class__("tt", 30, 10, 30)
        print(p)
    def eat(self, food):
        print("eat " + food)
    def say(self):
        print("Hello! my name if %s,I am %d years old"%(self.name, self.age))
    def play(a):#雖然可以用別的替代但不建議
        print("play",a.name)
    def __init__(self, name, age, height, weight):
        #print(name,age,height,weight)
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

per1 = Person("tom", 20, 160, 80)
per1.say()

per2 = Person("dongkun", 22, 160, 80)
per2.say()

per1.play()

per1.run()