n, m, k, t = map(int, input().split())
d = [0]*k
move = {
    'U' : (-1, 0),
    'D' : (1, 0),
    'L' : (0, -1),
    'R' : (0, 1)
}

def cau_distance(x, y): return sum([abs(x-d[i][0][0])+abs(y-d[i][0][1]) for i in range(k)])

for i in range(k):
    x, y = map(int, input().split())
    s = input()
    d[i] = [[x, y], s]

for i in range(t+1):
    print(min([cau_distance(j, k) for j in range(n) for k in range(m)]))
    if i == t: break
    for j in range(k):
        step = move[d[j][1][i]]
        d[j][0][0] = max(min(d[j][0][0]+step[0], n), 1)
        d[j][0][1] = max(min(d[j][0][1]+step[1], m), 1)