def main():

    from sys import stdin
    from collections import deque

    e = stdin.readline

    n, k = map(int, e().split())
    values = list(map(int, e().split()))
    values.append(0)
    sum_value = sum(values)
    dq = deque([[0, -1]])

    for i in range(n+1):

        while dq and dq[0][1] < i-k-1:

            dq.popleft()

        value = dq[0][0] + values[i]

        while dq[-1][0] > value:

            dq.pop()
        
        dq.append([value, i])
    
    print(sum_value - dq[0][0])

main()