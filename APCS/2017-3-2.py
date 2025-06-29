def main():
    from sys import stdin
    data = stdin.read().splitlines()
    index = 0
    k = int(data[index])
    index += 1
    s = [i.isupper() for i in data[index]]
    max_l = 0
    for i in range(len(s)):
        jndex = i
        c = 0
        now = s[i]
        while jndex < len(s):
            if s[jndex] != now:
                break
            jndex += 1
            c += 1
            if c == k:
                c = 0
                now = not now
        max_l = max(max_l, ((jndex - i)//k)*k)
    print(max_l)
main()