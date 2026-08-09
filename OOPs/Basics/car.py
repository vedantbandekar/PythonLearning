class Car:
    def __init__(self, model, year, color, for_sale): #constructor method to construct objects (dunder = double underscore)
        self.model = model
        self.year = year
        self.color = color 
        self.for_sale = for_sale

    def drive(self):  # methods are functions that belong to an object
        print(f"You drive the {self.color} color {self.model}")

    def stop(self):
        print(f"You stop the {self.color} color {self.model}")    

    def describle(self):
        print(f"I have a {self.color} {self.model} from year {self.year}")