"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""
class Rectangle:
    def __init__(self, __length, __width):
        self.__length = __length
        self.__width = __width
    def getarea(self):
        return f"area is {self.__length * self.__width}"
    def getPerimeter(self):
        return f"perimeter of {self.__width} width and {self.__length} length = {2*(self.__width + self.__length)}"
    def isSquare(self):
        return self.__width == self.__length
thefirstrectangle = Rectangle(30, 20)
print(thefirstrectangle.getarea())
thesecondrectangle = Rectangle(10, 10)
print(thesecondrectangle.isSquare())