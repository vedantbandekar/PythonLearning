# #Lists + indexing

# servers = ["Web-Server", "Database-Server", "File-Server", "DNS-Server"]

# ips = ["192.168.1.10", "192.168.1.20", "192.168.1.30", "192.168.1.40"]

# for i in range(len(servers)):
#     print(f"{servers[i]:15}--->{ips[i]}")

# #Dictionary + conditions

# devices = {
#     "Router-1": "up",
#     "Switch-1": "down",
#     "Server-1": "up",
#     "Access-Point-1": "down",
#     "Firewall-1": "up"
# }

# for key, value in devices.items():
#     if value == "down":
#         print(f"{key} is {value}")
    

# #Loop + condition + user input

# total = 0

# is_running = True
# while is_running:
#     user = int(input("Enter number: "))
#     if user == 0 :
#         break
#     else:
#         total += user

# print(f"Total: {total}")

# #Functions

# numbers = [45, 12, 89, 34, 67, 23]

# def max_number(numbers):
#     largest = numbers[0]
#     for number in numbers:
#         if number > largest:
#             largest = number
#     return largest

# print(max_number(numbers))


employees = {
    "Vedant": 45000,
    "Rahul": 52000,
    "Sneha": 38000,
    "Aarav": 61000,
    "Priya": 47000,
    "Rohan": 55000,
    "Ananya": 42000,
    "Karan": 68000,
    "Meera": 51000,
    "Aditya": 59000
}

list = []

while True:
    user = input("Enter name(q):")
    if user == "q":
        break
    else:
        for employee in employees:
            if employee == user:
                list.append(user)
            else:
                print("Employee not found")

