# Python Calculator

operation = input("Enter the operation (+ - * /)")
num1 = float(input("Enter 1st number:"))
num2 = float(input("Enter 2nd number:"))
# What i wrote
# if operation == "+" :
#     print(num1 + num2)
# elif operation == "-" :
#     print(num1 - num2)
# elif operation == "*":
#     print(num1 * num2)
# else:
#     print (num1/num2)

# How Bro wrote it 

if operation == "+" :
    result = num1 + num2
    print(round(result, 2))
elif operation == "-" :
    result = num1 - num2
    print(round(result, 2))
elif operation == "*":
    result = num1 * num2
    print(round(result, 2))
elif operation == "/":
    result = num1/num2
    print(round(result, 2))
else:
    print("Not a valid operation")

# Weight convertor

weight = float(input("Enter weight value:"))
unit = input("Enter weather pounds or kilogram(L / K): ")

if unit == "K":
    weight = weight * 2.205
    unit = "L"
    print(f"The weight {round(weight, 2)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs"
    print(f"The weight {round(weight, 2)} {unit}")
else:
    print(f"Invalid operation {unit}")

# Temperature Convertor 
# Same as weight convetor

unit = input("Enter temperature unit (F/C): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round ( (9 * temp)/5 + 32 , 2)
    print(f"The temperature in Fahrenheit is: {temp} ° F")
    # alt + 0176 = °
elif unit == "F":
    temp = round((temp-32) * 5/9 , 2)
    print(f"The temperature in Celcius is: {temp} ° C")
else:
    print(f"Invalid operation {unit}")


