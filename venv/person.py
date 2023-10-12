class Person:

    def __init__(self, name, age, country):
        self.__name = name
        self.__age = age
        self.__country = country

    def setName(self, userName):
        self.__name = userName
    def setAge(self, userAge):
        self.__age = userAge
    def setCountry(self, userCountry):
        self.__country = userCountry
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def getCountry(self):
        return self.__country

person = Person("John", "23", "Pula, Croatia")
x = person.getName()
y = person.getAge()
z = person.getCountry()
print(person.name)
print(x)
print(y)
print(z)
