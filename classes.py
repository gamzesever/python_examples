class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

#print(p1.name)
#print(p1.age)


class Student:
    def __init__(self, age, firstName, lastName):
        self.age = age
        self.fullname = firstName + " " + lastName
        self.surname = lastName
        self.firstname = firstName

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age

    def showAge(self):
        return self.fullname + " is " + str(self.age) + " years old"


p2 = Student(8, "vittiri", "guttiri")
print(p2.age)
print(p2.getAge())
print(p2.setAge(50))
print(p2.getAge())
"""
asd = p2.setAge(60)
print(p2.age)
print(p2.getAge())
p2.setAge(20)
print("setAge calisti...")
print(p2.age)
p2.setAge(40)
p2.age = 40

print(p2.age)
print(p2.getAge())
"""