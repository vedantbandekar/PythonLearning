# keyword arguments = an argument preceded by an identifier helps with readabilition order of arguments doesn't matter
# 1. positional 2. default 3. KEYWORD 4. arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

hello("Hello" , title = "Sir", first = "Lewis", last = "Hamilton")

for x in range(1,11):
    print(x, end=" ")

print("1","2","3","4","5", sep="-")