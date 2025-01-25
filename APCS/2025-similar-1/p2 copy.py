n, m, k, t = map(int, input().split())
d = [0]*k

if k%2 == 0: half = (k//2-1, k//2)
else: half = (k//2)

move = {
    'U' : (-1, 0),
    'D' : (1, 0),
    'L' : (0, -1),
    'R' : (0, 1)
}

for i in range(k):
    x, y = map(int, input().split())
    s = input()
    d[i] = [[x, y], s]

for i in range(t+1):
    xasix = [d[i][0][0] for i in range(k)]
    yasix = [d[i][0][1] for i in range(k)]
    xasix.sort()
    yasix.sort()
    mean_x = sum([xasix[i] for i in half])//2
    mean_y = sum([yasix[i] for i in half])//2
    print(mean_x, mean_y)
    print(sum([abs(i[0][0]-mean_x)+abs(i[0][1]-mean_y) for i in d]))
    if i == t: break
    for j in range(k):
        step = move[d[j][1][i]]
        d[j][0][0] = max(min(d[j][0][0]+step[0], n), 1)
        d[j][0][1] = max(min(d[j][0][1]+step[1], m), 1)