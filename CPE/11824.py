def main():
    from sys import stdin
    e = stdin.readline
    t = int(e().strip())
    for _ in range(t):
        d = []
        while True:
            i = int(e().strip())
            if i == 0: break
            d.append(i)
        d.sort(reverse=True)
        a = sum([2*(d[i]**(i+1)) for i in range(len(d))])
        if a > 5000000: print("Too expensive")
        else: print(a)
main()