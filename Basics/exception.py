# exception = An event that interrupts the flow of a program
# (ZeroDivisionError, TypeError, ValueError)
# 1.try, 2.except, 3.finally

try:
    number = int(input("Enter the number: "))
    print(1/number)
except ZeroDivisionError: #Use for zero division
    print("You can't divide by zero!")
except ValueError: #When input is int and user enters string
    print("You can only enter NUMBERS")
# except Exception: #Includes all exceptions but bad practice since user should know what is actually wrong 
#     print("Somethign went wrong")
finally: #It will execute always (Be there exception or not)
    print("Do some clean up here")