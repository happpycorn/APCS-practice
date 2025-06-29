def main():
    from sys import stdin
    e = stdin.readline
    n, k = map(int, e().split())
    d = {}
    dget = d.get
    dkeys = d.keys

    for i in list(map(int, e().split())):
        d[i] = dget(i, 0) + 1

    a = sorted(list(dkeys()))
    b = 0
    b_last = 0
    sum_len = 0
    for i in range(1, len(a)):
        b = b_last + (a[i]-a[i-1])*(sum_len + d[a[i-1]])
        sum_len += d[a[i-1]]
        if b > k: 
            break
        b_last = b
    k -= b
    print(k, a[i-1])
    
    sum_value = 1
    MOD_VALUE = 10**9 + 7
    for i in a:
        c = pow(i, d[i], MOD_VALUE)
        sum_value = sum_value*c % MOD_VALUE

main()