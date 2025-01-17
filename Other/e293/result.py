from math import gcd
d = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
q = 2305567963945518424753102147331756070
for _ in range(int(input())):
    n = int(input())
    s = gcd(n, q)
    if s == 1: print("Terrible Silence...")
    else: print(" ".join(map(str, [i for i in d if s%i == 0])))