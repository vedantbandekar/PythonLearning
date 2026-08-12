# Polymorphism = Greek word that means to "have many forms or faces"
# Poly = Many
# Morphe = Form

# TWO WAYS TO ACHIEVE POLYMORPHISM
# 1. Inheritance = An object could be treated of the sane typeras a parent class
# 2. "Duck typing" = Object must have necessary attributes/methods 

from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def Area():
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def Area(self):
        return self.side * self.side

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def Area(self):
        return self.height * self.base / 2

class Pizza(Circle):
    def __init__(self, toppings, radius):   #Since pizza is also consider a circle it is part of shapes and circle make it polymorph
        super().__init__(radius)
        self.toppings = toppings

    
shapes = [Circle(2), Square(2), Triangle(6, 4), Pizza("Corn", 15)]

for shape in shapes:
    print(f"{shape.Area()} cm²")

