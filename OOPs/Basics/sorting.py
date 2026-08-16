# SORTING IN PYTHON .sort() or sorted()
# Lists[], Tuples(), Dictionaries{"":""}, Objects

#============List==============

fruits = ["banana", "orange", "apple", "coconut"]

fruits.sort()
fruits.sort(reverse=True) #reverse order

print(fruits)

#============Tuple==============

fruits2 = {"banana", "orange", "apple", "coconut"}

fruits2 = sorted(fruits2)  #changes into a list
fruits2 = tuple(sorted(fruits2)) #typecast into tuple
fruits2 = tuple(sorted(fruits2, reverse=True)) #reverse order

print(fruits2)

#============Dictionray==============

fruits3 = {"banana": 105,
          "orange": 73,
          "apple": 72,
          "coconuts": 354}

fruits3 = dict(sorted(fruits3.items())) #sorting with key and value + typecasting
fruits3 = dict(sorted(fruits3.items(), key=lambda item: item[0], reverse=True)) # we take the key word than reverse
fruits3 = dict(sorted(fruits3.items(), key=lambda item: item[1])) # 0 means key used above and 1 means value used here
fruits3 = dict(sorted(fruits3.items(), key=lambda item: item[1], reverse=True)) # 0 means key used above and 1 means value used here

print(fruits3) 

#------------------Objects-----------------

class Fruits:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def __repr__(self):
        return f"{self.name} : {self.calories}"

fruits = [Fruits("banana", 105),
          Fruits("apple", 72), 
          Fruits("orange", 73),
          Fruits("coconut", 354)]

fruits = sorted(fruits, key=lambda fruits: fruits.name)
fruits = sorted(fruits, key=lambda fruits: fruits.name, reverse=True)
fruits = sorted(fruits, key=lambda fruits: fruits.calories)
fruits = sorted(fruits, key=lambda fruits: fruits.calories, reverse=True)

print(fruits)