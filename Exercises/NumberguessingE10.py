#Random number guessing game!

import random

lowest_no = 1
highest_no = 100
answer = random.randint(lowest_no, highest_no)

guesses = 0
running_pro = True

print("Python guessing game!")
print(f"Select a number between {lowest_no} and {highest_no}")
while running_pro:
    guess = input(f"Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < lowest_no or guess > highest_no:
            print("Not in range")
            print(f"Enter number between range of {lowest_no} and {highest_no}")
        elif guess < answer:
             print("Your guess is lower")
        elif guess > answer:
             print("Your guess is higher")
        else:
            print(f"CORRECT! It was {answer}")
            print(f"Number of guesses: {guesses}" )
            running_pro = False
    
    else:
        print("Invalid input")
        print(f"Enter number between {lowest_no} and {highest_no}")