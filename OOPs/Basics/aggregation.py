# Aggregation = Represents a relationship where one object (the whole)
# contains references to one or more INDEPENDENT objects (the parts)

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

library = Library("NewYork Library")

book1 = Book("Vagabond", "Takehiko Inoue")
book2 = Book("The Climber", " Shin-ichi Sakamoto")
book3 = Book("Harry Potter", "J.K. Rowling")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.name)

for book in library.list_books():
    print(book)


# Composition = The composed object directly owns its components, which cannot exist independently
# "owns-a" relationship

class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power)
        self.wheels = [Wheel(wheel_size) for wheel in range(4)] # this is list comprehension 

    def car_details(self):
        return f"{self.make} made {self.model} with {self.engine.horse_power} hp, wheel size {self.wheels[0].size} inch"


car1 = Car("Ford", "Mustang", 500, 18)
car2 = Car("Ferrari", "F40", 478, 16)

print(car1.car_details())
print(car2.car_details())