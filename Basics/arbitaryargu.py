# *args = allows you to pass multiple non-key arguments
# ** kwargs = allows you to pass multiple keyword-arguments * unpacking operator
# 1. positional 2. default 3. keyword 4. ARBITRARY

# def add(*args):  #you can write *nums or any name but people choose to use *args
#     total = 0
#     for arg in args:  #num in nums
#         total += arg
#     return total    

# print(add(1))

# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")

# print_address(building = "Signia Ocean",
#       city = "Navi Mumbai",
#       state = "Maharastra",
#       pin = "400708")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    # for value in kwargs.values():
    #     print(value, end = " ")
    if "apt" in kwargs:
        print(f"{kwargs.get('building')}, {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('city')}")
        print(f"{kwargs.get('pobox')}")
    
    else:
        print(f"{kwargs.get('building')}, {kwargs.get('city')}")
    
    print(f"{kwargs.get('state')}, {kwargs.get('pin')}")
 
shipping_label("Dr.", "Spongebob", "Squarepants","III",
        building = "Signia Ocean",
        pobox = "Po box #1001",
        city = "Navi Mumbai",
        state = "Maharastra",
        pin = "400708")



