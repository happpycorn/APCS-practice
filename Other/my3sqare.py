def main():
    from sys import stdin
    import math
    n = int(input())

    while n%4 == 0: n //= 4
    if n%8 != 7: return print("None")
    
    max_a = math.isqrt(n)