import datetime

date = datetime.date(2025, 9, 8)
today = datetime.date.today()

time = datetime.time(12,30,0)
now = datetime.datetime.now() #module.class.object

now = now.strftime("%H:%M:%S %d-%m-%Y")

# print(today)
# print(time)
# print(now)

target_datetime = datetime.datetime(2022, 1, 1, 6, 45, 25)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date time has passed")
else:
    print("Target date time has not passed")