# 快速冪、費馬小定理、mod inverse's feature、排容原理

def main():
    from sys import stdin
    e = stdin.readline
    N = 1005
    P = 1000000007
    fact = [1]*N
    inv = [1]*N
    content = []
    for i in range(1, N): fact[i] = (fact[i-1]*i)%P

    def modInverse(a, p):
        res = 1
        exp = p-2
        a = a%p
        while exp > 0:
            if exp&1 == 1: res = (res*a) % p
            a = (a*a)%p
            exp >>= 1
        return res

    inv[N-1] = modInverse(fact[N-1], P)
    for i in range(N-1, 0, -1): inv[i-1] = (inv[i]*i)%P

    def c(m, k):
        if k < 0 or k > m: return 0
        return (((fact[m] * inv[k]) % P) * inv[m-k]) % P
    
    for idx in range(int(e().strip())):
        n, m, k = map(int, e().split())
        res = 0
        neg = -1
        for i in range(m-k+1):
            neg *= -1
            res += (neg * c(m-k, i) * fact[n-k-i])%P
        res *= c(m, k)
        content.append(f"Case {idx+1}: {res%P}")
    
    print("\n".join(map(str, content)))
main()