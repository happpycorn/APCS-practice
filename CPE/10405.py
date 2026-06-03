def main():
    from sys import stdin
    e = stdin.readline
    content = []
    while True:
        a = e()
        if not a: break
        a = a.strip()
        b = e().strip()

        dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]

        for i in range(1, len(a)+1):
            for j in range(1, len(b)+1):
                if a[i-1] == b[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        content.append(dp[len(a)][len(b)])
    
    print("\n".join(map(str, content)))

main()