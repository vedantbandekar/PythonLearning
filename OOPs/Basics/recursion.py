# recursion = a function that calls itself from within
# helps to visualize a complex problem into basic steps
# problems can be solved more easily iteratively or recursively
# iterative = faster, complex
# recursive = slower, simpler

# ITERATIVE (This run in loops)

# def walk(steps):
    # for step in range(1, steps + 1):
        # print(f"You have took {step}") 

#RECUSION (This runs on conditon makinf the problem smaller with each step !!NOT GOOD FOR LARGE NUMBERS/PROCESS!!)
# def walk(steps):
#     if steps == 0:
#         return
#     # print(f"You have walked {steps}") #This will first print than go deeper i.e. Print first than perfrom the task 100 to 1 
#     walk(steps - 1)
#     print(f"You have walked {steps}") #this will go deeper than print i.e. starts case from 100 than goes till 0 and than print from 1 

# walk(100)

#Factorial

#Iteration

# def factorial(x):
#     result = 1
#     if x > 0:
#         for y in range (1, x + 1):
#             result *= y
#         return result

#Recursion

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)

print(factorial(10))