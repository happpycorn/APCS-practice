m, n, k = map(int, input().split())
d = [input() for _ in range(m)]
nd = [0]*m
score = 0
for _ in range(k):
    act = list(map(int, input().split()))
    for i in range(m):
        nd[i] = [d[i][(j-act[i])%n] for j in range(n)]
    for i in range(n):
        count_dict = {}
        for j in range(m):
            if nd[j][i] in count_dict.keys():
                count_dict[nd[j][i]] += 1
            else:
                count_dict[nd[j][i]] = 1
        score += max(count_dict.values())
    d = nd.copy()
print(score)