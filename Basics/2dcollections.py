
groceries = [["Apple","Banana","Mango","Tomato"],
             ["Onion","Potato","Garlic"],
             ["Chicken","Fish","Beef"]]

print(groceries[1][0])

for collection in groceries:  #for i in groceries:
    for food in collection:            #for i in j:
        print(food, end=(" "))                #print(j)
    print()
    