n, m = [int(i) for i in input().split()]

space = [0] * m

for _ in range(n):

    a, b, c = [int(i) for i in input().split()]

    c -= 1

    if a == 1:

        space[c] += b
    
    else:

        space[c] = max(0, space[c] - b)

print(" ".join(map(str, space)))