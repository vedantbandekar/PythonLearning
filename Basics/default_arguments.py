# # default arguments = A default value for certain parameters default is used when that argument is omitted make your functions more flexible, reduces # of arguments
# 1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

# def net_price(list_price, discount = 0, tax = 0.05):
#     return list_price * (1 - discount) * (1 + tax)

# print(net_price(2000))
# print(net_price(2000, 0.05))
# print(net_price(2000, 0.01, 0))

import time

def count(end, start=0):
    for x in range(start, end):
        print(x)
        time.sleep(1)
    print("Time's up!")

count(30, 15) #counts from 15 to 30
count(10)       #counts from 0 to 10
