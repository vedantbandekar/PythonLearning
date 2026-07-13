#Concession stand program (Threater popcorn stand)

menu = {"Pizza": 350,
        "Burger": 290,
        "Fries": 200,
        "Popcorn": 500,
        "Coke": 120,
        "Nachos": 150,
        "Sprite": 140}

cart = []
total = 0

print("------------MENU------------")

for key, value in menu.items():
    print(f"{key:20}:₹{value:.2f}")

print("------------------------------")


while True:  #while True checks for first condition to be true and 2nd to be false
    food = input("What will yoy like to have(Q to quit): ").capitalize()
    if food == "Q":
        print("Thankyou!")
        break
    elif menu.get(food) is not None:  #This will try to find food item from the menu i.e. potato in menu not there so none
        cart.append(food)

print("-----------TOTAL - BILL-------------")
for food in cart:
    total += menu.get(food)
    print(f"{food:15}... ₹{menu.get(food):.2f}")

print("------------------------------")

print(f"Total cost : ₹{total:.2f}")


    
