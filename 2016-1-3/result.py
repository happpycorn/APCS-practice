n = int(input())

l = []

for _ in range(n):
    s, e = map(int, input().split())
    l.append([s, "S"])
    l.append([e, "E"])

l.sort()
lc = 0
pos = 0
long = 0

for p, t in l:
    if t == "S":
        if lc == 0: pos = p
        lc += 1
    if t == "E":
        lc -= 1
        if lc == 0: long += p-pos

print(long)