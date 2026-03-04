m=int(input())

for _ in range(m):
    a,b,c=map(int,input().split())
    if b*b-4*a*c>=0 and int((b*b-4*a*c)**0.5)**2==b*b-4*a*c:
        print("Yes")
    else:
        print("No")