# "Duck typing" = Another way to achieve polymorphism besides Inheritance
# Object must have the minimum necessary attributes/methods
# "If it looks like a duck and quacks like a duck, it must be a dudklr"

class Animal:
    alive = True

class Dog(Animal):

    def speak(self):
        print("Woof!")

class Cat(Animal):
    
    def speak(self):
        print("Meow!")

class Duck(Animal):
    
    def speak(self):
        print("Quack!")

class Car:

    alive = False  #Since others are animal it has main parents function/attribute of being alive but car is another class therefore we define it here to that it fits in rather though it is unalive it honk i.e. speaks like animal one attribute matches

    def speak(self):  # Honk cha speak kela ki it becomes part of it (if it looks like a duck and quack like duck it is a duck) 
        print("Honk!")

animals = [Dog(), Cat(), Duck(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)