# 1
# n = int(input())

# sum = 0
# count = 0

# for i in range(1, n + 1):
#     if i % 3 == 0 or i % 5 == 0:
#         sum = sum + i
#         count = count + 1

# print("quantity:", count)
# print("sum:", sum)

# if count > 0:
#     print("average:", sum / count)
# else:
#     print("average: 0")


# 2
# n = int(input("N = "))

# suma =0
# count = 0
# max = 0
# min = 0

# while n >0:
#     digit = n % 10
#     suma += digit
#     count += 1
#     if digit > max:
#         max = digit
#     if min == 0 or digit < min:
#         min = digit
#     n //= 10

# print("sum:", suma)
# print("count:", count)
# print("max:", max)
# print("min:", min)


# 3
# n = int(input("N = "))

# for i in range(1, n + 1):
#     x = i
#     good = True

#     while x > 0:
#         digit = x % 10

#         if digit == 0:
#             good = False
#         elif i % digit != 0:
#             good = False

#         x //= 10

#     if good:
#         print(i, end=" ")

# 4

# height = int(input("height = "))
# width = int(input("width = "))
# inside_symbole = input("inside symbole = ")
# border_symbole = input("border symbole = ")
# if height < 3 or width < 3:
#     print("height and width must be greater than 2")
# for row in range(height):
#     for col in range(width):
#         if row == 0 or row == height - 1 or col == 0 or col == width - 1:
#             print(border_symbole, end="")
#         else:
#             print(inside_symbole, end="")
#     print()




