# read
n = int(input())
d = [[] for _ in range(n)]
ind = [0]*n
for _ in range(n-1):
    i, j = map(int, input().split())
    d[i].append(j)
    ind[j] += 1
# order
r = [i for i in range(n) if ind[i] == 0]
o = []
while r:
    i = r.pop(0)
    o.append(i)
    for j in d[i]:
        ind[j] -= 1
        if ind[j] == 0: r.append(j)
# count
dp = [None]*n
o.reverse()
for i in o:
    if len(d[i]) == 0: dp[i] = (0, 0); continue
    max_l = sec_l = -1*float("inf")
    max_c = 0
    for j in d[i]:
        nd = dp[j]
        if nd[0] > max_c: max_c = nd[0]
        if nd[1] >= max_l: sec_l, max_l = max_l, nd[1]
        elif nd[1] > sec_l: sec_l = nd[1]
    max_c = max(max_c, max_l+sec_l+2, max_l+1)
    dp[i] = (max_c, max_l+1)
print(max([dp[i][0] for i in range(n)]))