# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

user_name = input("Enter your username:")
digits = user_name.isdigit()

if len(user_name) > 12 :
    print("User name should not contain more than 12 characters")
elif not user_name.find(" ") == -1: #If your username is not -1 than it prints the following
    print("Username should not have any spaces")
elif not user_name.isalpha():
    print("Username should not contain an digits")
else:
    print(f"Your ussername is {user_name}")

