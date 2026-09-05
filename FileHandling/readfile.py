# Read files (.txt, .json, .csv)

# file_path = "output.txt"

# try:
#     with open(file_path, "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError: #When .txt is missed or wrong file type
#     print("That file was not found")
# except PermissionError: #Wehn not have permission to read that file
#     print("You do not have permission to read that file")

#For JSON
# import json

# file_path = "output.json"

# try:
#     with open(file_path, "r") as file:
#         content = json.load(file)
#         print(content)
#         print(content["name"])
#         print(content["age"])
#         print(content["job"])
# except FileNotFoundError: #When .txt is missed or wrong file type
#     print("That file was not found")
# except PermissionError: #Wehn not have permission to read that file
#     print("You do not have permission to read that file")

#For CSV
import csv

file_path = "output.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file) #only this give memory address
        for line in content:
            # print(line)
            print(line[0])
            # print(line[1])
            # print(line[2])

except FileNotFoundError: #When .txt is missed or wrong file type
    print("That file was not found")
except PermissionError: #Wehn not have permission to read that file
    print("You do not have permission to read that file")