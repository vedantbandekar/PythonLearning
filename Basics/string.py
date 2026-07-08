name = input("Enter your full name:")

length = len(name)
find = name.find(" ")
lastfind = name.rfind("a")
Capname = name.capitalize()
uppername = name.upper()
lowername = name.lower()
ifdigit = name.isdigit() # Checks is string is all digits 
ifalpha = name.isalpha() # Checks if it is all alphabet even space and gives boolen output
count = name.count("a")
# index = name.index(" ")  #?? exercise 6
name_replace = name.replace("vedant" , "Anushka")

print(length)
print(find)
print(lastfind)
print(Capname)
print(uppername)
print(lowername)
print(ifdigit)
print(ifalpha)
print(count)
print(name_replace)
# print(index)

