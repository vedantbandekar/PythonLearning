# return = statement used to end a function and send result back to the caller

# def add(x, y):
#     z = x + y
#     return z

# def multiply(x, y):
#     z = x * y
#     return z

# print(add(3, 4))
# print(multiply(2, 6))

def full_name (first_name, last_name):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    return first_name + " " + last_name

complete_name = full_name("vedant", "bandekar")
print(complete_name)