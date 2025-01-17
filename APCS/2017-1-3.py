n = int(input())
direction = int(input())
d = [input().split() for _ in range(n)]
directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
ans = []
x = y = n//2

for i in range(n-1):
    for _ in range(i+1):
        ans.append(d[x][y])
        x += directions[direction][0]
        y += directions[direction][1]
    direction = (direction+1)%4
    for _ in range(i+1):
        ans.append(d[x][y])
        x += directions[direction][0]
        y += directions[direction][1]
    direction = (direction+1)%4
for _ in range(i+2):
    ans.append(d[x][y])
    x += directions[direction][0]
    y += directions[direction][1]

print("".join(ans))
