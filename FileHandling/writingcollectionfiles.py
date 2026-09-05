# Writing collection files (List)

file_path = "EmployeeList.txt"

employees = ["Mark", "Jackson", "Mike", "Katty"]

with open(file_path, "w") as file:
    for i, employee in enumerate(employees, start = 1): #Or just employees if you dont want number list
        file.write(f"{i}. {employee}\n ")
    print(f"Text file '{file_path}' created")    