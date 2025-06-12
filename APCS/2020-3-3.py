def main():
    from sys import stdin
    data = stdin.read().splitlines()
    index = 0
    m, n = map(int, data[index].split())
    index += 1
    d = [None]*n
    for i in range(m):
        d[i] = list(map(int, data[index].split()))
        index += 1
    dp = [0]*n

    for i in range(m):
        left_max = [float("-inf")]*n
        right_max = [float("-inf")]*n
        for j in range(n):
            left_max[j] = d[i][j] + max(dp[j], left_max[j-1])
            right_max[-j-1] = d[i][-j-1] + max(dp[-j-1], right_max[-j])
        for j in range(n):
            dp[j] = max(left_max[j], right_max[j])
    print(max(dp))
main()