k = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
a = 0
while k > 0:
    a += k
    if a%x1 == 0: k-= y1
    if a%x2 == 0: k-= y2
print(a)