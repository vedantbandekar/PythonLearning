# class variables = Shared among all instances of a class
# Defined outside the constructor
# Allow you to share data among all objects created fron that class  

class Student:

    class_year = 2024 #Varibale class defined outside the constructor
    num_student = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_student += 1  #Track number of student we add

student1 = Student("Mark", 21)
student2 = Student("Spoongbob", 22)
student3 = Student("Bob", 24)

print(f"{student1.name}")
print(f"{student1.age}")
print(f"{Student.class_year}") #Use class name instead of any one student (instance)

print(f"Number of students: {Student.num_student}")
print(f"My graduating class of {Student.class_year} has {Student.num_student} students")