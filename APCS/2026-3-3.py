def main():
    from sys import stdin
    e = stdin.readline

    n, k = map(int, e().split())
    miss = list(map(int, e().split()))
    dist = [list(map(int, e().split())) for _ in range(n)]

    dp = [[-1]*(k+1) for _ in range(k+1)]
    for i in range(k):
        for j in range(i):
            dp[i][j] = max(
                dp[i-1][k] + dist[][]
                for k in range(j)
            )



    stack = [(k, k, 0, 0)]

    while len(stack) > 0:
        a, b, pos_a, pos_b = stack.pop()
        if b > a: a, b = b, a
        min_value = float("inf")
        for i in range(k+1):
            if dp[pos_a][i] == -1:
                stack.append((pos_a, i))
                stack.append((a, b))
            min_value = min(
                min_value, 
                dp[pos_a][i]+dist[pos_a][a+1]
            )


main()