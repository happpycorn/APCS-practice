def main():
    from sys import stdin
    e = stdin.readline

    l = []
    while s := e():
        s = s.lower()
        c = ''
        for i in s:
            if i.isalpha():
                c += i
            else:
                l.append(c)
                c = ''

    S = sorted(set(l))
    print('\n'.join(map(str, S[1:])))
main()