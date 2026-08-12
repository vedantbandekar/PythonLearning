# super() = Function used in a child class to call methods from a parent class (superclass).
# Allows you to extend the functionality of the inherited methods
 
class Shape:
    def __init__(self, is_filled, color):
        self.is_filled = is_filled
        self.color = color

    def describe(self):
        print(f"It is {self.color} and {"filled" if self.is_filled else "not filled"}")

class Circle(Shape):
    def __init__(self, is_filled, color, radius):
        super().__init__(is_filled, color)
        self.radius = radius

    def describe(self):
        super().describe() #Extend the functionality of the describe method (adds parent function to child)
        print(f"The area of the circle is {3.14 * self.radius * self.radius :.2f}cm^2")

class Square(Shape):
    def __init__(self, is_filled, color, width):
        super().__init__(is_filled, color)
        self.width = width

    def describe(self): # since we didnt not use super method it will not carry the functionality of parent
        print(f"The area of the square is { self.width * self.width :.2f} cm^2")

class Triangle(Shape):
    def __init__(self, is_filled,color, width ,height):
        super().__init__(is_filled, color)
        self.width = width
        self.height = height

circle = Circle(True, "Red", 24)
square = Square(is_filled = False, color = "Blue", width = 12)
triangle = Triangle(True, "Green", 16, 14)

circle.describe()
square.describe()
triangle.describe()