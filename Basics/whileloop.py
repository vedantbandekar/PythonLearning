# while loop = execute while condition is True 

#-----------------------------------------------

name = input("Enter your name:")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name:")

print(f"Hello {name}")

#-----------------------------------------------

age = int(input("Enter your age: "))

while age < 0 or age > 70 :
    print(f"Your age is not valid")
    age = int(input("Enter your age again: "))
    
print(f"You are Welcome!")

# -----------------------------------------------

food = input("Enter the food you like: ")

while not food  == "q":
    print(f"You like {food}")
    food = input("Enter the another food you like: ")

print("Bye!")

#-------------------------------------------------

num = int(input("Enter a number between 1-10: "))

while num < 1 or num > 10 :
    print(f"Number {num} is not valid")
    num = int(input("Try again number between 1-10: "))

print(f"Your number is {num}")

