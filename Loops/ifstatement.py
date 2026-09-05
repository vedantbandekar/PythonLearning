# if = Do some code only IF the condition is True Else do something else

age = int(input("Enter you age:"))

if age >= 70:
    print("You are too old for this")
elif age >= 18:
    print ("You are now signed up")
elif age <= 0:
    print ("You havent being born yet")
else:
    print ("You must be 18+")

# In terms of string

response = input("Would you like food (Y/N): ")

if response == "Y" :
    print ("Have some food")
else:
    print ("No food for you")

# -----------------------------------------

name = input("Enter your name: ")

if name == "":
    print ("You did not enter you name")
else:
    print (f"Hello {name}")

# Boolen terms for if else

online = True

if online:
    print ("You are online")
else:
    print ("You are offline")


