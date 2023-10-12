class Student:

    def __init__(self, name, studentclass, rollnumber, marks):
        self.__name = name
        self.__studentclass = studentclass
        self.__rollnumber = rollnumber
        self.__marks = marks

    def setName(self, studentName):
        self.__name = studentName
    def setClass(self, studentClass):
        self.__studentclass = studentClass
    def setRoll(self, rollNumber):
        self.__rollnumber = rollNumber
    def setMarks(self, studentMarks):
        self.__marks = studentMarks

    def calculateGrade(self):
        if self.__marks == "A":
            return "90-100 points"
        elif self.__marks == "B":
            return "70-89 points"
        elif self.__marks == "C":
            return "40-70 points"
        else:
            return "0-39 points"

    def getName(self):
        return self.__name
    def getClass(self):
        return self.__studentclass
    def getRoll(self):
        return self.__rollnumber
    def getMarks(self):
        return self.__marks

student = Student("Mike", "12D", "120", "")
print(student.calculateGrade())


