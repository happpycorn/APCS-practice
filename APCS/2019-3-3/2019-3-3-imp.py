n = int(input())
d = list(map(int, input().split()))

pre = [0] * (n+1)
for i in range(n): pre[i+1] = pre[i] + d[i]

swp = [(d[i], i) for i in range(n)]
swp.sort()

l = 0
r = n
swp_idx = 0

while True:

    while True:
        if l <= swp[swp_idx][1] < r:
            min_idx = swp[swp_idx][1]
            break
        swp_idx += 1

    left_sum = pre[min_idx] - pre[l]
    right_sum = pre[r] - pre[min_idx+1]

    if left_sum > right_sum: r = min_idx
    else: l = min_idx+1

    if l+1 == r: break

print(d[l])
