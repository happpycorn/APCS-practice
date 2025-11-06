def main():
    from sys import stdin
    e = stdin.readline

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

    n = int(e().strip())
    d = map(int, e().strip().split())
    idx_d = [[-1]*2 for _ in range(n+1)]

    for idx, i in enumerate(d):
        if idx_d[i][0] == -1: idx_d[i][0] = idx+1
        else: idx_d[i][1] = idx+1
    
    sum_v = 0
    bt = BIT(n*2)

    for i in range(n):
        
        sum_v += bt.range_query(idx_d[i+1][0], idx_d[i+1][1])
        bt.update(idx_d[i+1][0], 1)
        bt.update(idx_d[i+1][1], 1)
    
    print(sum_v)
main()