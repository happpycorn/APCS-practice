def main():
    from sys import stdin
    e = stdin.readline
    n = int(e())
    d = list(map(int, e().split()))

    tree = [0] * (4*n)

    def build(node, l, r):
        if l == r: tree[node] = l
        else:
            mid = (l+r)//2
            build(node*2, l, mid)
            build(node*2+1, mid+1, r)
            if d[tree[node*2]] < d[tree[node*2+1]]: tree[node] = tree[node*2]
            else: tree[node] = tree[node*2+1]
    
    def query(node, l, r, ql, qr):
        if qr < l or r < ql: return -1
        if ql <= l and r <= qr: return tree[node]
        mid = (l+r)//2
        lIdx = query(node*2, l, mid, ql, qr)
        rIdx = query(node*2+1, mid+1, r, ql, qr)
        if lIdx == -1: return rIdx
        if rIdx == -1: return lIdx
        return lIdx if d[lIdx] < d[rIdx] else rIdx

    build(1, 0, n-1)
    pre = [0] * (n+1)
    for i in range(n): pre[i+1] = pre[i]+d[i]

    l = 0
    r = n

    while True:
        if l+1 == r: break
        mid = query(1, 0, n-1, l, r-1)
        if pre[mid]-pre[l] > pre[r]-pre[mid+1]: r = mid
        else: l = mid+1
    
    print(d[l])

main()