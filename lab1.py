#1
# a = int(input())
# if a % 2 == 0:
#     print("even")
# else:
#     print("odd")

# age = int(input("Enter your age: "))

# if age >= 18:
#     print("you`re adult")
# else:
#     print("you`re not adult")


# r = int(input("Enter radius: "))
# s = 3.14 * r ** 2
# l = 2 * 3.14 * r
# print("Area: ", s)
# print("Length: ", l)

# a = int(input("Enter a number: "))
# b = int(input("Enter 2 number: "))
# if a > b:
#     print(a)
# if b > a:
#     print(b)
# else:
#     print("equal")

#2
#
# x,y = map(int, input("Enter 2 numbers: ").split())
# if x > 0 and y > 0:
#     print("1st quarter")
# elif x < 0 and y > 0:
#     print("2nd quarter")
# elif x < 0 and y < 0:
#     print("3rd quarter")
# elif x > 0 and y < 0:
#     print("4th quarter")

#3
# age = int(input("enter your age: "))

# if 11 <= age % 100 <= 14:
#     print(str(age) + " років")
# elif age % 10 == 1:
#     print(str(age) + " рік")
# elif 2 <= age % 10 <= 4:
#     print(str(age) + " роки")
# else:
#     print(str(age) + " років")


#4

# N, k, p1, p2 = map(int, input().split())
# a = (N // k) * p2 + (N % k) * p1
# b = (N // k + 1) * p2
# print(min(a, b))
