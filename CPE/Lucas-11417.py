from sys import stdin

def GCD(i,j):
    if i%j == 0:
        return j
    else:
        return GCD(j,i%j)


while True:
    n = int(stdin.readline())
    if n == 0:
        break
    total = 0
    for a in range(1,n):
        for b in range(a+1,n+1):
            total += GCD(b,a)
    print(total)