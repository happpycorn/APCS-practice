n, k = map(int, input().split())
values = list(map(int, input().split()))
values.append(0)
sum_value = sum(values)
dq = [[0, -1]]

for i in range(n+1):

    while dq[0][1] < i-k-1:

        dq.pop(0)

    value = dq[0][0] + values[i]

    while dq[-1][0] > value:

        dq.pop(-1)
    
    dq.append([value, i])

print(sum_value - dq[0][0])