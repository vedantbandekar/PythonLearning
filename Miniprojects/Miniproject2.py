# Calculating interest rate (Compound interest calculator)

principle = 0
rate = 0
time = 0

while principle <= 0 :  # while True: when you want = 0
    principle = float(input("Enter the principle amount: ₹"))
    if principle <= 0:
        print("Principle amount can not be less than or equal to zero")
    #when add while True 
    #else:
    #    break 

while True : #therefore this can be zero
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Rate amount can not be less than or equal to zero")
    else:
        break

while time <= 0 :
    time = float(input("Enter the time: "))
    if time <= 0:
        print("Time amount can not be less than or equal to zero")

total = principle * pow((1 + rate/100), time)
print(f"Your interest rate over {time} year/s : ₹ {total:.2f}")

