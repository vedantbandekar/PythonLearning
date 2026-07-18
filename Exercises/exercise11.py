import random

options = ("rock","paper","scissors")
count = 0
rounds = 0
running = True

print("Welcome to ROCK PAPER SCISSORS GAME!")

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter (Rock, Paper, Scissors):").lower()

    print(f"Your choice: {player}")
    print(f"Computer's choice: {computer}")

    if player == computer:
        print("It's a Tie!")
    elif player == "rock" and computer=="scissors":
        print("You Win!")
        count+=1
    elif player == "paper" and computer=="rock":
        print("You Win!")
        count+=1
    elif player == "scissors" and computer=="paper":
        print("You Win!")
        count+=1
    else:
        print("You lose!")

    print(f"Your score: {count}")
    rounds +=1
    print(f"Rounds: {rounds}")

    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")

