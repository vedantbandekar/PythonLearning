#ATM Menu Simulation 

print("Welcome to Python ATM")

inital_balance = 5000
balance = inital_balance
total_deposit = 0
total_withdraw = 0
is_running = True

while is_running:

    print("1. Check Balance")
    print("2. Deposite")
    print("3. Withdraw")
    print("4. Exit")
    
    user = input("Choose option:")

    if user == "4":
        break
    elif user == "1":
        print(f"Your balance : {balance:.2f}")
    elif user == "2":
        while True:
            deposit = int(input("Enter amount to be deposited: "))
            if deposit <= 0:
                print("Invalid deposite!")
            else:
                total_deposit += deposit
                balance += deposit
                print("Deposit successful")
                break
    elif user == "3":
        while True:
            withdraw = int(input("Enter amount to withdraw : "))
            if withdraw <= 0 or withdraw > balance:
                print("Invalid input")
            else:
                total_withdraw += withdraw
                balance -= withdraw
                print("Withdrawal successful")
                break
    else:
        print("Invalid input! Try again")

print("---------Your summary---------")
print(f"Initial balance: {inital_balance}") 
print(f"Current balance: {balance}")
print(f"Total withdrawal: {total_withdraw}")
print(f"Total deposit: {total_deposit}")

print("Thank You! Have a nice day :)")
   



