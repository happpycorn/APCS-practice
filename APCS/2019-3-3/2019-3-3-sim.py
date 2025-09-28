n = int(input())
d = list(map(int, input().split()))

l = 0
r = n

while True:
    min_idx = l
    for i in range(l, r): min_idx = i if d[i] < d[min_idx] else min_idx

    left_sum = sum(d[l:min_idx])
    right_sum = sum(d[min_idx+1:r])

    if left_sum > right_sum: r = min_idx
    else: l = min_idx+1

    if l+1 == r: break

print(d[l])
