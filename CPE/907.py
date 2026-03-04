def main():
    from sys import stdin
    e = stdin.readline

    def bsearch(a, l, r, k):
        while l <= r:
            mid = int((l + r)/2)
            if possible(a, k, mid): l = mid + 1
            else: r = mid - 1
        return mid
    
    def possible(a, k, m):
        idx = 0
        dk = 0
        while idx < len(a):
            if dk > k: return True
            dm = 0
            while idx < len(a):
                if dm + a[idx] > m: break
                dm += a[idx]
                idx += 1
            dk += 1
        return False

    while True:
        s = e()
        if not s: break
        n, k = map(int, s.split())
        d = [int(e().strip()) for _ in range(n+1)]
        print(bsearch(d, min(d), sum(d), k))
        
main()