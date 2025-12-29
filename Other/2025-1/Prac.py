d = [1, 2, 3, 4] # 一個長度為 n 的陣列
n = len(d)
s = 0
q = [0]*(n+1)
for i in range(n):
    s += d[i]
    q[i] = s
def f(i, j):
    return q[j]-q[i-1]