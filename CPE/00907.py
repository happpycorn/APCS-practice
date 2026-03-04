def main():
    from sys import stdin
    e = stdin.readline

    def bsearch(a, k):
        l = max(a)
        r = sum(a)
        ans = r

        while l <= r:
            mid = (l+r)//2
            if possible(a, k, mid):
                ans = mid
                r = mid - 1
            else: l = mid + 1

        return ans
    
    def possible(a, k, m):
        d = 0
        ndist = 0

        for dist in a:
            if ndist + dist > m:
                d += 1
                ndist = dist
            else:
                ndist += dist
            
            if d > k: return False
        return True

    while True:
        s = e()
        if not s: break
        n, k = map(int, s.split())
        d = [int(e().strip()) for _ in range(n+1)]
        print(bsearch(d, k))
        
main()