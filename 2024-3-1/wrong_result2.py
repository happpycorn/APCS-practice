n = int(input())
a = [int(i) for i in input().split()]
w = [int(i) for i in input().split()]

sum = (a[0] ** 2) * a[2]
t = (a[1] ** 2) * a[3]

som = 0
h = 0
hf = 0

for i in range(n):

    if w[i] > sum:
        som = w[i] - sum
        if som >= t:
            h += (sum / a[0] ** 2) + (t / (a[1] ** 2))
            if h > hf:
                hf = h
                break
        else:
            h += (sum / a[0] ** 2) + (som / (a[1] ** 2))
            sum = 0
    else:
        sum -= w[i]
        h += w[i] / (a[0] ** 2)
        
    if h > hf:
        hf = h
    
    h = 0

print(int(hf))