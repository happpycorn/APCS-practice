def main():
    from sys import stdin
    e = stdin.readline

    while True:
        s = e().strip()
        if not s: break

        n, m = map(int, s.split())
        d = [0]*(n+2)
        for i in range(n+1): d[i+1] = d[i]+int(e().strip())

        def cut(lim):
            cu = 0
            cn = 0
            for i in d:
                if cn + i <= lim: cn += i
                else: 
                    cu += 1
                    cn = i
            return cu <= m
        
        l = max(d)
        r = sum(d)
        ans = r

        while l < r:
            mid = (l+r)//2
            if cut(mid): 
                ans = mid
                r = mid
            else: l = mid+1
        print(ans)
main()