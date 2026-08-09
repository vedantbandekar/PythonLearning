ip = "192.168.1.10"

print(ip.replace(".","-"))

command = "  ping 192.168.1.1  "

print(command.strip()) #remove front and back spacing

servers = ["Web", "Database", "DNS"]
print(servers.pop())#pops last value (remove by position)
servers.remove("Database")# removes by value
print(servers) 

numbers = [10, 20, 30, 40, 50]

numbers[2] = 100 #you update value in list like this 

print(numbers)

# employee = {
#     "name": "John",
#     "salary": 75000,
#     "role": "Engineer"
# }

employees = {
    "John": 75000,
    "Sarah": 45000,
    "Mike": 62000,
    "Alex": 30000
}

for key, value in employees.items():
    if value > 50000:
        print(f"{key} has salary {value} greater than 50000")

numbers = [12, 5, 8, 21, 30, 17, 4]

for number in numbers:
    if number > 10:
        print(number)

#parameter is placeholder and argument is actual value

def is_even(num):
    return num%2 == 0  #return gives us true and false 

print(is_even(10))