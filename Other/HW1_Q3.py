a = 0
for i, j in enumerate([int(input()) for _ in range(int(input()))]):
    a += j
    if a < 0:
        print(i+1) 
        break
else:
    print(a)