# read
n = int(input())
d = [[] for _ in range(n)]
for _ in range(n-1):
    i, j = map(int, input().split())
    d[i].append(j)
# count
dp = [None]*n
def find_value(i):
    if not dp[i] is None: return dp[i]
    if len(d[i]) == 0: dp[i] = (0, 0); return dp[i]
    max_l = -1*float("inf")
    sec_l = -1*float("inf")
    max_c = 0
    for j in d[i]:
        nd = find_value(j)
        if nd[0] > max_c: max_c = nd[0]
        if nd[1] >= max_l: sec_l, max_l = max_l, nd[1]
        elif nd[1] > sec_l: sec_l = nd[1]
    max_c = max(max_c, max_l+sec_l+2, max_l+1)
    dp[i] = (max_c, max_l+1)
    return dp[i]
for i in range(n): find_value(i)
print(max([dp[i][0] for i in range(n)]))