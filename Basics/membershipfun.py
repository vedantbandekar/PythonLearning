#Membership operators = used to test whether a value or varibale is found in a sequence (string, list, tuple, set, or dictionary)
#1, in 2. not in

word = "APPLE"

letter = input("Guess the letter in the secret word: ")

if letter in word:  #not in
    print(f"The is a {letter}")  #print(f"{letter} not found")
else:
    print(f"{letter} not found") #print(f"The is a {letter}")


students = {"Spongbob", "Goku", "May"}

student = input("Enter the name of the student: ")

if student in students:
    print(f"{student} is in list")
else:
    print(f"{student} is not in list")


grades = {"Sandy" : "A",
          "Mike" : "B",
          "Mark" : "A+",
          "Jack": "B+"}

student = input("Enter the name of students: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")


email = "Iwillcomeback@gmail.com"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")

