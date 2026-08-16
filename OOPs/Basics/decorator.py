# Decorator = A function that extends the behavior of another function
# w/o modifying the base function
# Pass the base function as an argument to the decorator

# @add_sprinkles
# get_ice_cream("vanilla")

def add_sprinkles(func):
    def wrapper(*args, **kwargs):  #we need this beocz we want to print both of functions when we call it
        print("You add sprinkles🧁")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs): #args and kwargs(keyword arguments) to add any number of arguments
        print("You add fudge 🫕")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_icecream(flavour):
    print(f"Here is your {flavour} ice cream 🍧")

get_icecream("vanilla")