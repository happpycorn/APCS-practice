def main():
    from sys import stdin
    data = stdin.read().splitlines()
    idx = 0
    content = []

    while idx < len(data):
        n, m = map(int, data[idx].split())
        idx += 1
        d = list(map(int, data[idx].split()))
        idx += 1

        all_v = sum(d)
        ave_v = all_v/2
        k = min(n, m)

        d = [i + 50 for i in d]
        
        max_sum = 100 * 50 + 1
        dp = [[False] * (max_sum) for _ in range(k + 1)]
        dp[0][0] = True

        for var in d:
            for i in range(k, 0, -1):
                for j in range(var, max_sum):
                    if dp[i-1][j-var]: dp[i][j] = True
        
        min_sum = float("inf")
        max_sum = float("inf")
        for i in range(len(dp[-1])):
            if dp[-1][i]:
                v = i-50*k
                min_sum = min(min_sum, v)
                max_sum = max_sum if abs(max_sum-ave_v) < abs(v-ave_v) else v

        min_value = min_sum * (all_v-min_sum)
        max_value = max_sum * (all_v-max_sum)

        content.append(f"{max_value} {min_value}")
    print("\n".join(content))
main()