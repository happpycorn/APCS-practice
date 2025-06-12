n,m = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
rest = 0
for i in range(m):
    sum_m = q[i]
    while sum_m > 0:
        # sum_m = sum_m - p[rest]
        # rest = (rest + 1)%n
        for k in range(rest,n):
            sum_m = sum_m - p[k]            
            if sum_m <= 0:
                if k != n-1:
                    rest = k+1
                else:
                    rest = 0
                break
            if k == n-1:
                rest = 0
print(rest)