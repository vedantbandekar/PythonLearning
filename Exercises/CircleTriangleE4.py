import math 

print("Finding Circle parameters")
r = float(input("Enter the radius of the circle:"))

circumference = 2 * math.pi * r
area = math.pi * pow(r , 2)

print(f"Thr circumference of the circle is {round(circumference, 2)}cm")
print(f"Area o the circle is {round(area , 2)}cm^2")

print("Finding Hypotenuse of triangle")
a = float(input("Enter side A:"))
b = float(input("Enter side B:"))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Therefore side C (Hypotenuse):{round(c , 2)}")




