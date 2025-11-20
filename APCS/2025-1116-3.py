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
        
    n = int(e())
    d = list(map(int, e().split()))
    b = [0]*n
    for i in range(n):
        b[d[i]-1] = i+1
    
    arr = BIT(n)
    for i in range(n): arr.update(i+1, 1)
    
    idx = 0
    jdx = 0
    sum_v = 0

    for i in b:
        jdx = i
        l = jdx if idx > jdx else idx
        r = jdx if idx < jdx else idx
        sum_v += arr.range_query(l, r)
        arr.update(jdx, -1)
        idx = jdx
    
    print(sum_v)
main()