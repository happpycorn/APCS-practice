n = int(input())
d = list(map(int, input().split()))
dp = [[None]*n for _ in range(n)]
for i in range(n): dp[i][i] = (0, d[i])
def find_value(i, j):
    if not dp[i][j] is None: return dp[i][j]
    min_value = (float('inf'), 0)
    for k in range(i, j):
        var1 = find_value(i, k)
        var2 = find_value(k+1, j)
        vart = (var1[0]+var2[0]+abs(var1[1]-var2[1]), var1[1]+var2[1])
        if vart[0] < min_value[0]: min_value = vart
    dp[i][j] = min_value
    return dp[i][j]
print(find_value(0, n-1)[0])