item = input("Enter the item you would like to buy: ")
price = float(input("Enter the price of the item: "))
quantity = int(input(f"Enter the amount of {item}/s you would like: "))

total = price * quantity 

print(f"You would like {item} x {quantity}")
print(f"So the total cost: ${round(total, 2)}")