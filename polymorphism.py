from cat import Cat
from mouse import Mouse
from person import Person
'''
多態:一種事物的多種形態
最終目標:人可以餵任何一種動物

'''

tom = Cat("tom")
jerry = Mouse("jerry")

tom.eat()
jerry.eat()

#思考:再添加100種動物都有name屬性和eat方法
#定義了一個有name屬性和eat方法的Animal類,讓所有動物繼承

#定義一個人類,可以餵貓跟老鼠吃東西
# per = Person()
# per.foodCat(tom)
# per.foodMouse(jerry)

#思考:人要餵100種動物難道要寫100個food方法?
#tom和jerry都繼承自動物
per = Person()
per.foodAnimal(tom)
per.foodAnimal(jerry)