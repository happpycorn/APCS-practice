def main():
    from sys import stdin
    e = stdin.readline
    n, r = map(int, e().strip().split(","))
    e()
    e()
    d = []
    for i in range(n):
        a = list(map(int, e().strip().split(",")))
        b = len(a)-a.count(0)
        c = sum(a)/b
        if (b/len(a))*100 >= r: d.append([c, n-i, len(a), sum(a)])
    d.sort(reverse=True)
    if len(d) > 0: print(f"{n-d[0][1]+1},{d[0][2]},{d[0][3]}")
    else: print(-1)
main()