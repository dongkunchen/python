from person import Person
from student import Student
from worker import Worker

per = Person("aa", 1, 10000)

stu = Student("dongkun", 18, 300000000, 1000)
print(stu.name, stu.age)
stu.run()
print(stu.stuId)
print(stu.getMoney())

wor = Worker("lilai", 20, 10000)
print(wor.name, wor.age)
wor.eat("apple")

print(per.getMoney())