#Python quiz game

questions = ("1. What is the 2nd planet from the Earth?",
             "2. Who lays world's largest eggs?",
             "3. What is the speed of light?",
             "4. How many elements are there in the periodic table?",
             "5. Which is strongest metal in the world")

options = (("A. Mars","B. Jupiter","C. Saturn","D. Uranus"),
           ("A. Ostriche","B. Snake","C. Whale","D. Chicken"),
           ("A. 3x10^-8","B. 3x10^10","C. 3x10^8","D. 5x10^6"),
           ("A. 110","B. 117","C. 118","D. 124"),
           ("A. Tungsten","B. Iron","C. Gold","D. Diamond"))

guessed = []
score = 0
solutions = ("B","A","C","C","A")
question_no = 0

for question in questions:
    print(question, end=" ")
    print()
    for answers in options[question_no]:
        print(answers)

        
    answer = (input("Answer:").upper())
    guessed.append(answer)
    if answer == solutions[question_no]:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect! The answer was {solutions[question_no]}")
    
    question_no += 1

print("The answer you guessed: ")
for guess in guessed:
    print(guess, end=" ")
print()

print("The actual answer are: ")
for solution in solutions:    
    print(solution, end=" ")
print()


print("---------------------")
print("       Result        ")
print("---------------------")
print(f"Total score:{(score/len(guessed))*100}%")


