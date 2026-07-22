#List comprehension = A concise way to create lists in python compact and easier to read than traditional loops [expression for the value in iterable if condition]

# double = []
# for x in range(1, 11);
#     double.append(x*2)

# print(double)

# #this above can be changed into 

# double = [x * 2 for x in range(1,11)]
# triple = [y * 3 for y in range(1, 11)]
# square = [z * z for z in range(1, 11)]

# print(double)
# print(triple)
# print(square)

# fruits = ["apple", "orange", "banana", "coconut"]
# fruits = [fruit.upper() for fruit in fruits]
# print(fruits)


# fruits = [fruit.upper() for fruit in ["apple", "orange", "banana", "coconut"]]
# print(fruits)

# fruits = ["apple", "orange", "banana", "coconut"]
# fruit_char = [fruit[0] for fruit in fruits]
# print(fruit_char)

# numbers = [-1,2,3,-4,5,-6]
# positive_num = [num for num in numbers if num >= 0 ]
# negetive_num = [num for num in numbers if num < 0 ]
# even_num = [num for num in numbers if num%2 == 0 ]
# odd_num = [num for num in numbers if num%2 == 1 ]

# print(positive_num)
# print(negetive_num)
# print(even_num)
# print(odd_num)

grades = [56, 48, 84, 92, 36, 75]

passing_grades = [grade for grade in grades if grade >= 48]
print(passing_grades)