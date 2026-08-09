# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
             "India": "New Delhi",
             "China": "Beijing",
             "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))

print(capitals.get("Japan"))
print(capitals.get("India"))

if capitals.get(input("Enter the captial:")):
    print("Capital exists")
else:
    print("Capital does not exist")

capitals.update({"Genmany": "Berlin"})
capitals.update({"USA": "Chicago"}) #can also update existing value
capitals.pop("China")
capitals.popitem() #last item
capitals.clear()

keys = capitals.keys() #Main components i.e. USA China etc
for key in capitals.keys():
    print(key)

values = capitals.values()
for value in capitals.values():
    print(value)

for key, value in capitals.items():
    print(f"{key} : {value}")



