# Logical operators = used on conditional statements
        # and = checks two or more conditions if True
        # or = checks if atleast one condition is True
        # not = True if condition is False, and vice versa

temp = 40

if temp > 0 and temp < 30 : 
    print("The temperature is good")
else:
    print("The temperature is bad")

# ----- conditions changes the formula/code changes

if temp <= 0 or temp >= 30 : 
    print("The temperature is bad")
else:
    print("The temperature is good")

# ---------Not conditions----------

sunny = False

if not sunny:
    print("Its cloudy outside")
else:
    print("Its sunny")
