# collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ["apple" , "orange" , "banana" , "coconut"]  #---List

fruitss = {"apple" , "orange" , "banana" , "coconut"}  #---Set

fruitsss = ("apple" , "orange" , "banana" , "coconut") #---Tuple

#--------------------Applied for all-------------------
print(dir(fruits)) #different methods that are available to collections
print(help(fruits)) #gives description of all the methods
print(len(fruits)) #no of elements within the list

print("apple" in fruits) #if value present in the list
print("pineapple" in fruits)
#--------------------Tuples-----------------------

print(fruitsss.index("apple")) #index of the item
print(fruitsss.count("coconuts")) #no of items

#--------------------Set------------------------

fruitss.add("pineapple") #adds
fruitss.removes("apple") #delete
fruitss.pop() #random element removes
fruitss.clear() #clear set

#--------------------List------------------------

fruits[0] = "pineapple" #fruits[0] is a index using this we can reassign the value
#i.e: apple becomes pineapple 
fruits.append("pineapple") # add element at the edn of list
fruits.remove("apple") # removes value from the list
fruits.insert(0, "pineapple") #addes pineapple in place of zero and shifts the list
fruits.sort() #list in alphabatical order
fruits.reverse() #reverse the order
fruits.clear() #clear list
print(fruits.index("apple")) #prints index of apple
print(fruits.count("banana")) #prints number of banana in the list

#----------------------------------------------

print(fruits[1]) #0,1,2,3
print(fruits[:3])
print(fruits[::2]) #every 2nd element
print(fruits[::-1]) #backwards

#----------------------------------------------

for fruit in fruits:
    print(fruit)

