m, n, k = map(int, input().split())
d = [input() * 2 for _ in range(m)]
score = 0
indexs = [0]*m
for _ in range(k):
    act = list(map(int, input().split()))
    for i in range(m): indexs[i] = (indexs[i]-act[i])%n
    for i in range(n):
        freq = {}
        max_count = 0
        for j in range(m):
            ch = d[j][i+indexs[j]]
            if ch in freq: freq[ch] += 1
            else: freq[ch] = 1
            max_count = max(max_count, freq[ch])
        score += max_count
print(score)
