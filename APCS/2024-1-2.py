# https://zerojudge.tw/ShowProblem?problemid=m932

m, n, k = map(int, input().split(" "))

a = [input() for _ in range(m)]

steps = list(map(int, input().split(" ")))

arrow = [(-1, 0), (0, 1), (1, 1), (1, 0), (0, -1), (-1, -1)]

h, w = m-1, 0

road = []

for step in steps:

    new_h, new_w = h + arrow[step][0], w + arrow[step][1]

    if 0 <= new_h < m and 0 <= new_w < n:

        h, w = new_h, new_w

    road.append(a[h][w])

pass_road = list(set(road))

print("".join(road))
print(len(pass_road))