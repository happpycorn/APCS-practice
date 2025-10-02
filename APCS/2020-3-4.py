def main():
    from sys import stdin
    e = stdin.readline

    class SegTree:
        def __init__(self, arr, func, default) -> None:
            self.n = len(arr)
            self.func = func
            self.default = default
            self.tree = [self.default]*(2*self.n)
            for i in range(self.n): self.tree[self.n+i] = arr[i]
            for i in range(self.n-1, 0, -1): self.tree[i] = func(self.tree[i*2], self.tree[i*2+1])

        def query(self, l, r):
            res = self.default
            l += self.n
            r += self.n
            while l < r:
                if l & 1:
                    res = self.func(res, self.tree[l])
                    l += 1
                if r & 1:
                    r -= 1
                    res = self.func(res, self.tree[r])
                l >>= 1
                r >>= 1
            return res

        def update(self, idx, value):
            idx += self.n
            self.tree[idx] = value
            while idx > 1: 
                idx >>= 1
                self.tree[idx] = self.func(self.tree[2*idx], self.tree[2*idx+1])

    n = int(e().strip())
    d = map(int, e().strip().split())
    arr = [0]*n
    st = SegTree(arr, lambda a,b: a+b, 0)
    f_r = [0]*n
    sum_v = 0

    for i in d:
        i -= 1
        if st.query(i, i+1):
            sum_v += st.query(0, i) - f_r[i]
            st.update(i, 2)
        else:
            f_r[i] = st.query(0, i)
            st.update(i, 1)
    
    print(sum_v)
main()