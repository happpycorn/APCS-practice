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

arr = [2, 1, 5, 3, 4]
st = SegTree(arr, func=min, default=float("inf"))

print(st.query(1, 4))  # 查詢 [1,4) = min(1,5,3) = 1
st.update(1, 6)        # arr[2] = 1 改成 6
print(st.query(1, 4))  # 現在 min(6,5,3) = 3
for i in range(len(arr)): print(st.query(i, i+1))
