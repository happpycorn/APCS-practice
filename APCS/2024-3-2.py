# https://zerojudge.tw/ShowProblem?problemid=o712

m, n, k, r, c = map(int, input().split())
data = [[int(i) for i in input().split()] for _ in range(m)]

face = 0
jewl = 0
score = 0
rotation = [(0, 1), (1, 0), (0, -1), (-1, 0)]


while 1:

    if data[r][c] == 0 : break

    score += data[r][c]
    jewl += 1

    data[r][c] -= 1

    if score % k == 0 : face += 1

    while 1:

        r1 = r+rotation[face%4][0]
        c1 = c+rotation[face%4][1]

        if 0 <= r1 < m and 0 <= c1 < n and data[r1][c1] != -1 : break
        else : face += 1
    
    r, c = r1, c1

print(jewl)