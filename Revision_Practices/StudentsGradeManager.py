#Students Grade Manager

students = []
marks = []

is_running = True

print("Students Grade Manager")

while is_running:
    print("1. Add Student")
    print("2. View Students")
    print("3. Calculate Average")
    print("4. Find Highest Score")
    print("5. Find lowest Score")
    print("6. Exit")

    user = input("Choose an option: ")

    if user == "6":
        print("Thank you!")
        break
    elif user == "1":
        student = input("Enter the name of the student: ")
        students.append(student)
        mark = int(input("Enter students marks: "))
        marks.append(mark)
    elif user == "2":
        print("-----------Students List------------")
        print(f"Name{" ":23}Marks")
        for i in range(len(students)):
            print(f"{i+1}. {students[i]:20}--- {marks[i]}")

        print("------------------------------------")
    elif user == "3":
        
        if not marks:
            print("No student added yet!")
        else:
            avg = sum(marks)/len(marks)
            print(f"The average marks: {avg:.2f}")
    elif user == "4":
        if not marks:
            print("No student added yet!")
        else:
            highest_score = max(marks)
            print(f"Highest score: {highest_score}")
    elif user == "5":
        if not marks:
            print("No student added yet!")
        else:
            lowest_score = min(marks)
            print(f"Lowest score: {lowest_score}")
    else:
        print("Invalid input!")



