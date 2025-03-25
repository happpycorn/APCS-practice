def main():
    from sys import stdin
    e = stdin.readline
    l = int(e().strip())
    d = list(map(int, e().strip().split()))
    s = 0
    for i in range(l):
        n = d[i]
        for j in range(i+1, l):
            if d[j] == n:
                s += j-i-1
                break
    print(s)
main()