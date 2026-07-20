#function = A block of resurabe code 
#           place () after the function name invoke

def happy_birthday(name, age):  #can change parameters name and age to x and y also!
    print(f"Happy Birthday to {name}")
    print(f"You are {age} years old!")
    print("Happy birthday to you!")
    print()

happy_birthday("Vedant", 20)
happy_birthday("Me", 20)

#-----------------------------------------------------

def display_invoice(name, amount, due_date ):
    print(f"Hello {name}!")
    print(f"Your paymenet amount ₹{amount:.2f} is going to due on {due_date}")

display_invoice("Steve" ,2000 , "01/04/2045")

