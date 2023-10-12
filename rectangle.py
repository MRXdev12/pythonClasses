class Rectangle:

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return (self.width + self.length) * 2

rectangle = Rectangle(2, 2)

print(rectangle.area())
print(rectangle.perimeter())
