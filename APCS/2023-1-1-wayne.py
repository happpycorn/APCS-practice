x,n=map(int,input().split())
d=list(map(int,input().split()))

big=0
max_b = x
small=0
min_s = x

for i in d:
    if i>x:
        big+=1
        max_b = max(i, max_b)
    else:
        small+=1
        min_s = min(i, min_s)

if big>small:
    print(big, max_b)
else:
    print(small, min_s)