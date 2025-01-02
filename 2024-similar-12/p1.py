t = int(input())

for _ in range(t):
    n = int(input())
    count = 0
    for i in range(1, n-2):
        for j in range(1, n-i):
            if n-i-j-i <= 0: break
            count += n-i-j-i
    print(count)