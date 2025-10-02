def main():
    from sys import stdin
    e = stdin.readline

    while True:
        s = e().strip()
        if not s: break

        n, m = map(int, s.split())
        d = [0]*(n+2)
        for i in range(n+1): d[i+1] = d[i]+int(e().strip())

        dp = [[-1]*(m+1) for _ in range(n+2)]
        for i in range(n+2): dp[i][0] = d[i]
        for i in range(m+1): dp[0][i] = 0

        for i in range(n+2):
            for j in range(min(i+1, m+1)):
                min_c = -1
                for k in range(i):
                    t = max(dp[k][j-1], d[i]-d[k])
                    if min_c == -1: min_c = t
                    else: min_c = min(min_c, t)
                dp[i][j] = min_c
        print(dp[n+1][m])
main()