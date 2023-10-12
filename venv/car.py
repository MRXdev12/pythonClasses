class Car:

    def __init__(self, company, model, year):
        self.__company = company
        self.__model = model
        self.__year = year

    def setCompany(self, companyName):
        self.__company = companyName

    def setModel(self, modelName):
        self.__model = modelName

    def setYear(self, selectYear):
        self.__year = selectYear

    def getCompany(self):
        return self.__company

    def getModel(self):
        return self.__model

    def getYear(self):
        return self.__year

car = Car("BMW", "SERIA 5", "2023")

x = car.getCompany()
print(x)

y = car.getModel()
print(y)

z = car.getYear()
print(z)