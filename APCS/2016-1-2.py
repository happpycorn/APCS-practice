r, c, m = map(int, input().split())
a = [[int(i) for i in input().split()] for _ in range(r)]
b = [int(i) for i in input().split()]

b.reverse()

def flip(a : list):    
    return [a[-i-1] for i in range(len(a))]

def turn(a : list):
    r, c = len(a), len(a[0])
    return [[a[i][-j-1] for i in range(r)] for j in range(c)]

for i in b:
    a = flip(a) if i else turn(a)

r, c = len(a), len(a[0])

print(r, c)

for i in a:

    st = " ".join(map(str, i))

    print(st)