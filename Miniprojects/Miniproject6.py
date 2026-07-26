#Python Banking Program

#1. show balance
#2. Deposite
#3. Withdraw

def show_balance(balance): # goes here and from here it goes in main (here balance is parameter)
    print(f"Your balance is ₹{balance:.2f}")   #so balance from here 

def deposit():
    amount = float(input("Enter the amount to deposite:"))

    if amount < 0:
        print("Invalid amonut. Try again!")
        return 0
    else:
        return amount 

def withdraw(balance):
    amount = float(input("Enter an amount to withdrawal: "))

    if amount > balance:
        print("Insufficient amonut. Try again!")
        return 0
    elif amount < 0:
        print("Invalid input")
        return 0
    else:
        return amount

def main():
    balance = 0 #and updated over here
    is_running = True

    while is_running:
        print()
        print("******************************")
        print("    Welcome to PythonBank    ")
        print()
        print("******************************")
        print()
        print(" 1. Check Balance")
        print(" 2. Deposite")
        print(" 3. Withdrawal")
        print(" 4. Exit")
        print()

        choice = input("Please select a option: ")

        if choice == "1":
            show_balance(balance) #here that balance is matched (here balance is argument when value is assigned)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance) 
        elif choice == "4":
            is_running = False
        else:
            print("Invalid choice/input. Try again!!")

    print("Thank-You! Have a nice day :)")

if __name__ == "__main__": #use this is this program is runned it will run main
    main() 