n, k = [int(i) for i in input().split()]

dp = [int(i) for i in input().split()]

sum_dp = [sum(dp[0:i]) for i in range(len(dp))]

dp_result = {}

def hug(start, end):

    if start == end:

        return dp[start]
    
    if dp_result.has_key(f"{start}+{end}"):

        return dp_result[f"{start}+{end}"]
    
    max_value = 0

    for i in range(end-start):
    
        result = hug(start, start+i) + hug(start+i+1, end)

        max_value = max(result, max_value)

    return max_value

print(hug(0, len(dp)))