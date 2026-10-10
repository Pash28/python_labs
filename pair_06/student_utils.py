import random
import statistics as st

def grades(count):
    rates = []
    for i in range(0, count):
        rates.append(random.randint(1,12))
    return rates

def average(grades):
    return round(st.mean(grades), 1)

def level(average):
    if average >= 10 and average <= 12:
        return "excellent"
    if average >= 7 and average < 10:
        return "good"
    if average >= 4 and average < 7:
        return "satisfactory"
    else:
        return "bad"