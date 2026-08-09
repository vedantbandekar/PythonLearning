# object = A "bundle" of related attributes (variables) and methods (functions)
# Ex. phone, cup, book
# You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

from car import Car

car1 = Car("Ferrari",1999 , "red", False)
car2 = Car("Merc",2014 , "silver", False)
car3 = Car("BMW",2026 , "yellow", True)

print(car1) # gives memory object
print(car2.model) # . is attribute access
print(car2.color)
print(car2.year)  
print(car2.for_sale)

car1.drive() #same for 1 2 3 car
car2.stop()

car1.describle()