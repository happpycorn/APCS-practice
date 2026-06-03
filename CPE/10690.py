# DP、位元操作
def main():
    from sys import stdin
    e = stdin.readline
    content = []

    while True:
        t = e().strip()
        if not t: break
        n, m = map(int, t.split())
        d = list(map(int, e().split()))

        all_v = sum(d)
        k = min(n, m)

        d = [i + 50 for i in d]
        
        dp = [0 for _ in range(k + 1)]
        dp[0] = 1

        for var in d:
            for i in range(k, 0, -1):
                dp[i] |= (dp[i-1] << var)
        
        min_value = float("inf")
        max_value = float("-inf")
        max_possible_sum = k * 100 
        for i in range(max_possible_sum + 1):
            if (dp[-1] >> i) & 1:  
                v = i - 50 * k
                current_product = v * (all_v - v)
                min_value = min(min_value, current_product)
                max_value = max(max_value, current_product)

        content.append(f"{max_value} {min_value}")
    print("\n".join(content))
main()