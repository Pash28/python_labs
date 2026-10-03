#1
# numbers = [12, -7, 0, 5, -9, 18, 4, -3]
# positive_numbers = []
# negative_numbers = []
# even_numbers = []
# divide3 = []

# for number in numbers:
#     if number > 0:
#         positive_numbers.append(number)
#     if number < 0:
#         negative_numbers.append(number)
#     if number % 2 == 0:
#         even_numbers.append(number)
#     if number % 3 == 0:
#         divide3.append(number)

# print("starting list:", numbers)
# print("Positive numbers:", positive_numbers)
# print("Negative numbers:", negative_numbers)
# print("Even numbers:", even_numbers)
# print("Numbers divisible by 3:", divide3)
# print("Minimum value:", min(numbers))
# print("Maximum value:", max(numbers))
# print("Sum:", sum(numbers))
# print("Average:", sum(numbers) / len(numbers))

#2

# group1 = {"Anna", "Ivan", "Olha"}
# group2 = {"Ivan", "Maksym", "Olha"}

# group3 = group1 & group2
# group1_only = group1 - group2
# group2_only = group2 - group1
# unique = group1 | group2

# print("joint:", ' '.join(group3))
# print("group1_only:", ' '.join(group1_only))
# print("group2_only:", ' '.join(group2_only))
# print("unique:", ' '.join(unique))

#3
# products = {
#     "milk": 20,
#     "bread": 15,
#     "eggs": 30,
#     "chocolate": 120,
#     "mango": 150
# }



# name = input("Enter product name: ")
# price = int(input("Enter product price: "))
# products[name] = price

# name = input("Enter product name to search: ")
# price = products.get(name)

# if price is not None:
#     print("Price:", price)
# else:
#     print("Product not found")

# min_price = float(input("min: "))
# max_price = float(input("max: "))

# print("products in diapazon:")

# for name, price in products.items():
#     if min_price <= price <= max_price:
#         print(name, "-", price)



#4
# students = {
#     'Ivan': [10, 11, 12, 9, 10],
#     'Anna': [8, 9, 10, 11, 9]
# }

# group = ('10-IT', '2026\\2027')

# best_name = ""
# best_grade = 0

# print(f"Group: {group[0]}, {group[1]}")

# print("Group book:")
# for name, marks in students.items():
#     print(f"{name}: {marks}")

# name = input("Enter the name of the new student: ")
# marks = input("Enter 5 grades separated by comma: ")

# grades = []
# for mark in marks.split(','):
#     grades.append(int(mark.strip()))

# correct = True

# if len(grades) != 5:
#     correct = False
# else:
#     for mark in grades:
#         if mark < 1 or mark > 12:
#             correct = False
#             break

# if correct:
#     students[name] = grades

#     print(f"Student {name} added")

#     print("Updated group book:")
#     for name, marks in students.items():
#         print(f"{name}: {marks}")

#     print("Average grades:")
#     rating = []

#     for name, marks in students.items():
#         average = sum(marks) / len(marks)

#         print(f"{name}: {average}")

#         rating.append((average, name))

#         if average > best_grade:
#             best_grade = average
#             best_name = name

#     rating.sort(reverse=True)

#     print("Rating:")
#     for average, name in rating:
#         print(f"{name}: {average}")

#     print("The best student is:", best_name, best_grade)

# else:
#     print("Error")

