N, k, p1, p2 = map(int, input().split())
a = (N // k) * p2 + (N % k) * p1
b = (N // k + 1) * p2
print(min(a, b))