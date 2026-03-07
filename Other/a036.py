def main():
    from sys import stdin
    e = stdin.readline
    n, r = map(int, e().split())
    r = min(r, n - r)
    if r < 0:
        print(0)
        return
    if r == 0:
        print(1)
        return
    dp = [0] * (r + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(min(i, r), 0, -1):
            dp[j] = dp[j] + dp[j-1]       
    print(dp[r])
main()