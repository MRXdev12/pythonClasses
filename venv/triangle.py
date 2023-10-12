class Triangle:

    def __init__(self, lengthLine1, lengthLine2, lengthLine3):
        self.__lengthLine1 = lengthLine1
        self.__lengthLine2 = lengthLine2
        self.__lengthLine3 = lengthLine3

    def isEquilateral(self):
        if (self.__lengthLine1 == self.__lengthLine2) and (self.__lengthLine1 == self.__lengthLine3) and (self.__lengthLine2 == self.__lengthLine3):
            return True
        else:
            return False

    def isIsoscel(self):
        if (self.__lengthLine1 == self.__lengthLine2) or (self.__lengthLine1 == self.__lengthLine3) or (self.__lengthLine2 == self.__lengthLine3):
            return True
        else:
            return False
    def isScalene(self):
        if not self.isIsoscel():
            return True

        else:
            return False

triangle = Triangle(2, 3, 4)
print(triangle.isEquilateral())
print(triangle.isIsoscel())
print(triangle.isScalene())