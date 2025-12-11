class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, i, delta):
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def range_query(self, l, r):
        return self.query(r) - self.query(l - 1)

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

class HeapNode:
    def __init__(self): self.heap = []

    def get_parent_index(self, i): return (i - 1) // 2

    def swap(self, i, j): self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, value):
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)

    def _bubble_up(self, index):
        raise NotImplementedError("not define")