'''
重寫:將函數重寫定義寫一遍
__str__()
__repr__()
注意:在沒有str時且有repr repr=str
'''
class Person(object):
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def __str__(self):
        return "%s-%d-%d-%d" %(self.name,self.age,self.height,self.weight)

per = Person("dongkun", 20, 172, 62)
print(per)

#重點:當對象的屬性值很多可以寫__str__