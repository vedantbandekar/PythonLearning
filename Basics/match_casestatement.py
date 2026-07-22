#Match-case statement (switch): An alternative to using many 'elif' statements Execute some code if a value matches a 'case' 
# Benefits: clearer and syntax is more readable


# def day_of_week(day):
#     if day == 1:
#         return "Its Sunday"
#     elif day == 2:
#         return "Its Monday"
#     elif day == 3:
#         return "Its Tuesday"
#     elif day == 4:
#         return "Its Wednesday"
#     elif day == 5:
#         return "Its Thrusday"
#     elif day == 6:
#         return "Its Friday"
#     elif day == 7:
#         return "Its Saturday"
#     else:
#         return "Invalid input"

# user = int(input("Enter number (1-7): "))    
# print(day_of_week(user))
# Here this above code is replaced elif with cases and match using match_case

# def day_of_week(day):
#     match day:
#         case 1:
#             return "Its Sunday"
#         case 2:
#             return "Its Monday"
#         case 3:
#             return "Its Tuesday"
#         case 4:
#             return "Its Wednesday"
#         case 5:
#             return "Its Thrusday"
#         case 6:
#             return "Its Friday"
#         case 7:
#             return "Its Saturday"
#         case _:  #wild card
#             return "Invalid input"

# user = int(input("Enter number (1-7): "))    
# print(day_of_week(user))

def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thrusday" | "Friday" :
            return False
        case _:
            return False
        
print(is_weekend("Sunday"))
