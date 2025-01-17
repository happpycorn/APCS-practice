n, k, m = map(int, input().split())
def isOdd(n, k):
    while k > 0:
        if k & 1 > n & 1: return False
        n >>= 1
        k >>= 1
    return True
if m >= n: print(0)
else:
    d = list(map(int, input().split()))[m:m+k+1]
    a = 0
    for index, value in enumerate(d): # 最多 10^5
        # 取 C
        if index > k-index: index = k-index
        if isOdd(k, index): a = a ^ value
    print(a)