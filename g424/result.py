def main():

    from sys import stdin
    e = stdin.readline

    n, k = map(int, e().split())
    dp = list(map(int, e().split()))

    sum_dp = [0] * n
    sum_result = [0] * n

    sum_value = 0

    for i in range(n):

        sum_value += dp[i]
        sum_dp[i] = sum_value

    sum_result[:k] = sum_dp[:k]

    for i in range(k, n):

        sum_result[i] = max([sum_result[i-j-1] + sum_dp[i] - sum_dp[i-j] for j in range(k+1)])

    print(sum_result[-1])

main()