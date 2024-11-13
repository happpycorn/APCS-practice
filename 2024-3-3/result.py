m, n, q = map(int, input().split())

data = []

for i in range(m):

    data.append(list(map(int, input().split())))
    if -2 in data[i]:
        r0, r1 = i, data[i].index(-2)

done = [[0]*n for _ in range(m)]

def ignite(r, c, done):

    if not 0 <= r < m or not 0 <= c < n or done[r][c]:

        return 0
    
    done[r][c] = 1

    ignite_count = 1

    area = data[r][c]

    for i in range(-area, area+1):
        for j in range(-area, area+1):
            if abs(i)+abs(j) < area: ignite_count += ignite(r+i, c+j, done)
    
    return ignite_count

ignite_count = 0

radius = 0

while ignite_count < q:

    radius += 1

    for i in range(-radius, radius+1):
        for j in range(-radius, radius+1):
            if abs(i)+abs(j) < radius: ignite_count += ignite(r0+i, r1+j, done)

print(radius-1)