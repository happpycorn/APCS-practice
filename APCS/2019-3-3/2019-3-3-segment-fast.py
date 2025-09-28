def main():
    from sys import stdin
    e = stdin.readline
    n = int(e())
    d = list(map(int, e().split()))

    # iterative segment tree (store indices)
    size = n
    tree = [0] * (2 * size)

    # build: 放索引
    for i in range(n):
        tree[size + i] = i
    for i in range(size - 1, 0, -1):
        l, r = tree[i << 1], tree[i << 1 | 1]
        if d[l] < d[r]:
            tree[i] = l
        else:
            tree[i] = r

    # query [l, r]
    def query(l, r):
        l += size
        r += size + 1
        res = -1
        while l < r:
            if l & 1:
                if res == -1 or d[tree[l]] < d[res]:
                    res = tree[l]
                l += 1
            if r & 1:
                r -= 1
                if res == -1 or d[tree[r]] < d[res]:
                    res = tree[r]
            l >>= 1
            r >>= 1
        return res

    # 前綴和
    pre = [0] * (n + 1)
    for i in range(n):
        pre[i + 1] = pre[i] + d[i]

    l = 0
    r = n
    while True:
        if l + 1 == r:
            break
        mid = query(l, r - 1)
        if pre[mid] - pre[l] > pre[r] - pre[mid + 1]:
            r = mid
        else:
            l = mid + 1

    print(d[l])


main()
