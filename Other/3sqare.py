a=int(input())
A=[]
for i in range(3):
    A.append(int(a**0.5))
    a-=A[-1]**2
if a>0:
    print('none')
else:
    A.reverse()
    print(*A)