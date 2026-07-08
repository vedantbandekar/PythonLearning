# Conditional Expressions = A shortcut for the if-else statement (ternary operator) 
# Print or assign one of the two values based on a condition x if condition else y 

num = 5
a = 6
b = 7
age=21
temperature = 26
user_role = "admin"

print ("Positive" if num > 0 else "Negetive")

result = "EVEN" if num % 2 == 0 else "ODD"
print(result)

max_num = a if a > b else b
min_num = a if a < b else b
print(max_num)
print(min_num)

status = "Adult" if age >= 18 else "Child"
print(status)

weather = "Hot" if temperature > 25 else "Cold"
print(weather)

access_level = "Full Access" if user_role == "admin" else "Partial Access"
print(access_level)