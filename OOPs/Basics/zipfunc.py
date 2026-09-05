# zip() = Combines multiple iterables (lists, tuples, sets, dict)
# into a single iterator.
# Makes managing multiple indices easier

names = ["Simon", "Mark", "JJ"]
ages = [31, 25, 45]
jobs = ["Youtuber", "Film-maker", "Retried"]

data = zip(names, ages, jobs) #converts into an object(zip is an object)

for name, age, job in data:
    print(f"{name} is {age} year old and {job}")