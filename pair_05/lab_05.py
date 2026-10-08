#1
# p = 3.14159
# def circle_area(radius):
#     return p * radius ** 2

# def rectangle_area(width, height):
#     return width * height

# def triangle_area(base, height):
#     return 0.5 * base * height

# def main():
#     print("Choose a shape to calculate area: 1. Circle 2. Rectangle 3. Triangle")
#     ch = int(input("Enter your choice (1-3): "))
#     if ch == 1:
#         radius = float(input("Enter radius: "))
#         print(f"Area of the circle is {circle_area(radius)}")
#     elif ch == 2:
#         width = float(input("Enter width: "))
#         height = float(input("Enter height: "))
#         print(f"Area of the rectangle is {rectangle_area(width, height)}")
#     elif ch == 3:
#         base = float(input("Enter base: "))
#         height = float(input("Enter height: "))
#         print(f"Area of the triangle is {triangle_area(base, height)}")

# main()


#2
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True

# def divisors(n):
#     divs = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             divs.append(i)
#     return divs

# def digit_sum(n):
#     return sum(map(int, str(abs(n))))


# n = int(input("Number: "))

# print("Prime:", is_prime(n))
# print("Divisors:", divisors(n))
# print("Digit sum:", digit_sum(n))


#3

# def average(numbers):
#     return sum(numbers) / len(numbers)


# def above(numbers, limit):
#     count = 0

#     for n in numbers:
#         if n > limit:
#             count += 1

#     return count


# grades = []

# for i in range(5):
#     grades.append(float(input("Grade: ")))

# limit = float(input("Limit: "))

# print("Average:", average(grades))
# print("Minimum:", min(grades))
# print("Maximum:", max(grades))
# print("Above limit:", above(grades, limit))


#4

# def len_password(password):
#     if len(password) < 8:
#         return "Password is too short"

# def has_uppercase(password):
#     for char in password:
#         if char.isupper():
#             return True
#     return False

# def has_lowercase(password):
#     for char in password:
#         if char.islower():
#             return True
#     return False

# def has_digit(password):
#     for char in password:
#         if char.isdigit():
#             return True
#     return False

# def has_special_char(password):
#     special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
#     for char in password:
#         if char in special_chars:
#             return True
#     return False

# def is_valid_password(password):
#     if len_password(password):
#         return len_password(password)
#     if not has_uppercase(password):
#         return "Password must contain at least one uppercase letter"
#     if not has_lowercase(password):
#         return "Password must contain at least one lowercase letter"
#     if not has_digit(password):
#         return "Password must contain at least one digit"
#     if not has_special_char(password):
#         return "Password must contain at least one special character"
#     return "Password is valid"