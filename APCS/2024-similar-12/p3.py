# read
n, m = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(n)]
# sum
d_sum = [[0]*m for _ in range(n+1)]
for i in range(n): d_sum[i] = [d[i][j] + d_sum[i-1][j] for j in range(m)]
# count
max_value = 0
for i in range(n):
    for j in range(i, n):
        nd = [d_sum[j][k] - d_sum[i-1][k] for k in range(m)] # sum
        dp = [0]*m
        for k in range(m): dp[k] = nd[k] + max(dp[k-1], 0)
        max_value = max(max(dp), max_value) # update
print(max_value)