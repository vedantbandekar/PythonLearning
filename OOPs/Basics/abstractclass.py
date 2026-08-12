# Abstract class: A class that cannot be instantiated on its own; Meant to be subclassed.|
# They can contain abstract methods, which are declared but have no implementation.
# Abstract classes benefits:
# 1. Prevents instantiation of the class itself
# 2. Requires children to use inherited abstract methods

from abc import ABC, abstractmethod

class Vehicle(ABC):  # its kind of set of rules which every childer has to follow

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# vehicle = Vehicle() # this wont work 

class Car(Vehicle):
    
    def go(self):
        print("Car is going")

    
    def stop(self):
        print("Car has stopped")

class Bike(Vehicle):
    
    def go(self):
        print("You are riding bike")

    
    def stop(self):
        print("You stopped the bike")

class Boat(Vehicle):
    
    def go(self):
        print("Boat is sailing")

    
    def stop(self):
        print("Boat is anchored")

car = Car()
bike = Bike()
boat = Boat()

car.go()
car.stop()
bike.go()
bike.stop()
boat.go()
boat.stop()

