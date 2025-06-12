n,m = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

d = [0]*(2*n+1)
for i in range(n*2):
    d[i] = d[i-1] + p[i%n]

rest = 0
for i in range(m):
    start = rest-1
    end = rest
    while d[end]-d[start] < q[i]:
        end += 1
    rest = (end+1)%n

print(rest)