def main():
    from sys import stdin
    e = stdin.readline
    n, m = map(int, e().strip().split())
    ad = {}
    for _ in range(n):
        d = e().strip()
        k = d[0]+d[-1]
        if k in ad.keys():
            ad[k].append(d)
        else:
            ad[k] = [d]
    write = [""]*m
    max_len = 0
    c = 0
    for key in sorted(ad.keys()):
        a = 0
        for val in ad[key]:
            if a == 0 or c == 0: k = key
            else: k = ""
            write[c] = f"{write[c]}{' '*(max_len-len(write[c]))}{k:<3}{val}"
            c += 1
            if a == 0: a = 1
            if c == m:
                c = 0
                max_len = max([len(i) for i in write])+1
    for i in write:
        print(i)
main()