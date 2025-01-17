def main():
    from sys import stdin
    e = stdin.readline
    while True:
        i = list(map(int, e().split()))
        if any(i) == 0: break
        t1 = 60*i[0]+i[1]
        t2 = 60*i[2]+i[3]
        print(t2-t1 if t2 >= t1 else 60*24-t1+t2)
main()