def mod_factorial(x, p):

    result = 1

    for i in range(1, x + 1):
        result = (result * i) % p

    return result

m, n, k = map(int, input().split())

p = 1145141

numerator = mod_factorial(m + n - 2, p)
denominator_m = mod_factorial(m - 1, p)
denominator_n = mod_factorial(n - 1, p)

denominator = (denominator_m * denominator_n) % p
denominator_inv = pow(denominator, p - 2, p)

print((numerator * denominator_inv) % p)