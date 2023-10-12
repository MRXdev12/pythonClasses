class Date:

    def __init__(self, day, month, year):
        self.__day = day
        self.__month = month
        self.__year = year

    def setDay(self, currentDay):
        self.__day = currentDay

    def setMonth(self, currentMonth):
        self.__month= currentMonth

    def setYear(self, currentYear):
        self.__year = currentYear

    def isValid(self):
        if (1 <= self.__day <= 31) and (1 <= self.__month <= 12) and (self.__year > 0):
            return True
        else:
            return False

    def getDay(self):
        return self.__day
    def getMonth(self):
        return self.__month
    def getYear(self):
        return self.__year

date = Date(12, 12, 1999)
print(date.isValid())