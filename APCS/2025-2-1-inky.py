k = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

c = [x1*i for i in range(1, 30)]
d = [x2*i for i in range(1, 30)]

a = 0
while k > 0:
    a += k
    for i in c:
        if a == i:
            k -= y1
    for i in d:
        if a == i:
            k -= y2

print(a)