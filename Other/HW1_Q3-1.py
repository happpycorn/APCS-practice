a = 0
b = []
c = False
for i, j in enumerate([int(input()) for _ in range(int(input()))]):
    a += j
    if a < 0:
        b.append(i+1)
        c = True
b.append(a)
print(b[int(c)-1])