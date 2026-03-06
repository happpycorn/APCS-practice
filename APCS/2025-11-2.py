def main():
    from sys import stdin
    e = stdin.readline
    n = int(e().strip())
    d = [
        list(map(int, e().split())) 
        for _ in range(n)
    ]

    from itertools import permutations
    i = range(0, n)
    order = list(permutations(i, n))

    def bsearch(a, o, l, r):
        ans = l
        while l <= r:
            mid = (l+r)//2
            if any(check(a, i, mid) for i in o): 
                ans = mid
                l = mid+1
            else:
                r = mid-1
        return ans
    
    def check(a, o, x):
        start, end, during = a[o[0]]
        st = start + during
        if st > end: return False
        for i in range(1, len(o)):
            start, end, during = a[o[i]]
            if max(st + x, start) + during > end: return False
            st = max(st + x, start) + during
        return True

    last = max(list(zip(*d))[1])-sum(list(zip(*d))[2])
    print(bsearch(d, order, 0, last))
main()