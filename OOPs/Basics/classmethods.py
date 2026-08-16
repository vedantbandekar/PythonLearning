# Class methods = Allow operations related to the class itself
# Take (cls) as the first parameter, which represents the class itself.


class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    #INSTANCE METHOD
    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod   #This is used to access the things that are present in the class and not or each individual object
    def get_count(cls):
        return f"Total # of students: {cls.count}"

    @classmethod
    def get_avg_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa:{cls.total_gpa / cls.count:.2f}"

student1 = Student("Spongbob", 3.2)
student2 = Student("Pattick", 2.0)
student3 = Student("Sandy", 4.5)

print(Student.get_count())
print(Student.get_avg_gpa())