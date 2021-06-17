from person import Person

class Student(Person):
    def __init__(self, name, age, money, stuId):
        #調用父類中的__init__
        super(Student, self).__init__(name, age, money)
        self.stuId = stuId
    def stuFunc(self):
        print(self.__money)