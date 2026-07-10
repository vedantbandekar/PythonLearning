#Shopping cart

foods = []
prices = []
total = 0

while True:
    food = input("Enter the food you would like(Q to quit): ")
    if food.upper() == "Q":
        break
    else:
        price = int(input("Enter the price you like: "))
        foods.append(food)
        prices.append(price)
    
print("#-------Your Cart---------#")

for i in range(len(foods)):
    print(i, f"{foods[i]:20}------₹{prices[i]}")


for price in prices:
    total += price

print(f"Your total bill is : {total}")



