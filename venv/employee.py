class Employee:

    def __init__(self, name, employeeid, salary):
        self.__name = name
        self.__employeeid = employeeid
        self.__salary = salary

    def setName(self, employeeName):
        self.__name = employeeName

    def setEmployeeId(self, employeeID):
        self.__employeeid = employeeID

    def setSalary(self, employeeSalary):
        self.__salary = employeeSalary

    def calculateSalary(self, performance):
        if performance >= 0 and performance <= 10:
             self.__salary = performance * self.__salary
             return self.__salary

        else:
            return "You are fired Nigga"

    def getName(self):
        return self.__name
    def getEmployeeId(self):
        return self.__employeeid
    def getSalary(self):
        return self.__salary

employee = Employee("Mike", "12", 1000)
print(employee.calculateSalary(5))