def main():
    from sys import stdin
    e = stdin.readline
    d = [[-1]*(502) for _ in range(501)]
    def gcd(d, i, j):
        if d[i][j] != -1: return d[i][j]
        if i % j == 0: d[i][j] = j; return j
        else: d[i][j] = gcd(d, j, i%j); return d[i][j]
    while True:
        n = int(e())
        if n == 0: break
        g = 0
        for i in range(1, n):
            for j in range(i, n):
                g += gcd(d, j+1, i)
        print(g)
main()