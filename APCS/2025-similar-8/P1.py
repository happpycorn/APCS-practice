def main():
    from sys import stdin
    e = stdin.readline
    c = int(e().strip())
    d = list(map(int, e().split()))
    d.reverse()

    idx = 0
    sum_v = 0
    while idx < c:
        if d[idx] < 11:
            sum_v += 1
            idx += 2
        else:
            idx += 1
    
    print(sum_v)
main()