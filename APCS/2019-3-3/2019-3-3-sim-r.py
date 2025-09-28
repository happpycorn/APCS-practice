n = int(input())
d = list(map(int, input().split()))

def f(l, r):
    if l+1 == r: return d[l]

    min_idx = l
    for i in range(l, r): min_idx = i if d[i] < d[min_idx] else min_idx

    left_sum = sum(d[l:min_idx])
    right_sum = sum(d[min_idx+1:r])

    if left_sum > right_sum: return f(l, min_idx)
    else: return f(min_idx+1, r)

print(f(0, n))
