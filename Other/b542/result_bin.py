n, q = map(int, input().split())

d = list(map(int, input().split()))
d.sort()

for _ in range(q):
    i = int(input())

    finded = False
    for j in range(n):
        l = j
        r = n - 1
        while l <= r:
            m = (l+r)//2
            if d[m]-d[j] == i:
                finded = True
                break
            elif d[m]-d[j] > i: r = m-1
            elif d[m]-d[j] < i: l = m+1
        if finded: break
    
    if finded: print("YES")
    else: print("NO")