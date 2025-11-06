def main():
    from sys import stdin
    e = stdin.readline
    while True:
        d = e()
        if not d: break
        a, b = map(int, d.split())
        print(a^b)

main()