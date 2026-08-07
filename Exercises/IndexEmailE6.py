email = input("Enter your email: ")

index = email.index("@")

username = email[:index]
domain = email[index + 1:]

print(f"Your username is {username} and domain is {domain}")
#  .index is same as .find but if not found .find gives -1 where as .index error
