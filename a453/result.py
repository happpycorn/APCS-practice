import math
n = int(input())
for _ in range(n):
    a, b, c = map(int, input().split())
    sqr = b*b - 4*a*c
    if a == 0: print("No")
    elif sqr >= 0 and int(math.sqrt(sqr))**2 == sqr: print("Yes")
    else: print("No")