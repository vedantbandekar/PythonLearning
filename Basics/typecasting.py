# Typecasting = The process of converting a value of one data type to another (string, integer, float, boolen)
# Types 2 : Explicit vs Implicit

me = "Vedant"
age = 22
gpa = 9.2
student = True

print(type(me))
print(type(age))
print(type(gpa))
print(type(student))

# Explicit 
age = float(age)
print(age)
print(type(age))

student = str(student)
print(student)
print(type(student))

age = bool(age)
print(age)

me = bool(me)
print (me)

#Implicit 
x = 2
y = 0.5

x = x/y
print (x)
print(type(x))
