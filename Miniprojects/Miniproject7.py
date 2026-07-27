#Slot machine python

import random

def spin_row():
    symbols = ['🍒', '🔔', '🍉', '⭐', '🍋']

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("*****************")
    print(" | ".join(row))
    print("*****************")

def payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 4
        elif row[0] == "🍉":
            return bet * 1
        elif row[0] == "⭐":
            return bet * 3
        elif row[0] == "🍋":
            return bet * 2
    else:
        return 0

def main():

    balance = 100
    spin = 0
    total_won = 0
    total_bet = 0

    print("***********************")
    print("Welcome to Slot machine")
    print("Symbols : 🍒 🔔 🍉 ⭐ 🍋")
    print("***********************")

    while balance > 0:

        print(f"Your balance is ₹{balance}")

        bet = input("Enter you bet: ")

        if not bet.isdigit():
            print("Invalid input! Enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient balance. Try again!")
            continue

        if bet <= 0 :
            print("Bet should be more than 0")
            continue

        balance -= bet
        total_bet += bet
        spin += 1

        row = spin_row()
        print("Spinning....")
        print_row(row)

        won = payout(row, bet)

        if won > 0:
            total_won += won
            balance += won
            print(f"You won ₹{won}")
        else:
            print("You lost!")

        user = input("Want to spin again? (Y/N): ").upper()

        if user == "Y":
            continue
        else:
            break

    print(f"Game over! Your final balance is ₹{balance}")
    print(f"You have spun {spin} times!")
    print(f"You have won ₹{total_won}")
    print(f"You have bet ₹{total_bet}")


if __name__ == "__main__":
    main()