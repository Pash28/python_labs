#a = 12
#b = 12.4
#c = 'hello'
#d = True
#
#print(a + b)

#a = int(input())
#b = int(input())
#
#print(int(a) + int(b)) #конкатинація

#a = int(input("#1 "))
#b = int(input("#2 "))
#c = int(input("#3 "))
a, b, c = map(int, input("enter 3 numbers: ").split())


if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
elif c > a and c > b:
    print(c)
else:
    print("equal")