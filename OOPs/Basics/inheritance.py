# Inheritance = Allows a class to inherit attributes and methoos from another cilss
# Helps with code reuspbility and extensibility
# class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eatting(self):
        print(f"{self.name} is eatting")

    def sleeping(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Mouse(Animal):
    def speak(self):
        print("Squeek!")

dog = Dog("Scooby")
cat = Cat("Tom")
mouse = Mouse("Jerry")

print(dog.name)
print(dog.is_alive)
cat.eatting()
dog.sleeping()
mouse.speak()

#Here animal class has a main class and Dog Cat Mouse are part of that class insteadd of self we write Animal in () which interitance the main animal class and according to the object it will display what they speak


