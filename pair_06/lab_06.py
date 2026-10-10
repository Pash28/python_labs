
#1

# import math

# r = int(input("radius: "))
# catets = list(map(int, input("enter two catets: ").split(',')))
# total = int(input("Number of items: "))
# per_pack = int(input("Items per pack: "))

# print(f"circle area: {round(math.pi * r ** 2, 2)}")
# print(f"gipotenusa: {math.hypot(catets[0], catets[1])}")
# print(f"required packs: {math.ceil(total / per_pack)}")





#2
# import random
# import statistics

# count = int(input("How many grades? "))
# grades = []

# for _ in range(count):
#     grades.append(random.randint(1, 12))

# print(grades)
# print(f"Minimum: {min(grades)}")
# print(f"Maximum: {max(grades)}")
# print(f"Average: {round(statistics.mean(grades), 1)}")
# print(f"Median: {statistics.median(grades)}")




#3

# from datetime import date

# year = int(input("enter year: "))
# month = int(input("enter month: "))
# day = int(input("enter day: "))

# event_date = date(year, month, day)
# today = date.today()

# difference = (event_date - today).days

# if difference > 0:
#     print(f"till event: {difference} days")
# elif difference < 0:
#     print(f"after event: {abs(difference)} days")
# else:
#     print("event is today!")



