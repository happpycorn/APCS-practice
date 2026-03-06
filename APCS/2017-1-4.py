def main():
    from sys import stdin
    e = stdin.readline

    def bsearch(a, l, r, x):
        ans = r
        while l <= r:
            mid = (l+r)//2
            if x < gready(a, mid): l = mid+1
            else: 
                ans = mid
                r = mid-1
        return ans

    def gready(a, x):
        num = 1
        lp = a[0]
        for di in a:
            if lp + x < di:
                num += 1
                lp = di
        return num
    
    n, k = map(int, e().split())    
    d = list(map(int, e().split()))
    d.sort()

    print(bsearch(d, 1, d[-1]-d[0], k))

main()