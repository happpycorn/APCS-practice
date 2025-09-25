def f(arr, n):
    if not n: return print(*arr)
    for i in n:
        if all(
            abs(idx - len(arr)) != abs(value - i) 
            for idx, value in enumerate(arr)
        ): f(arr+[i], n-{i})

n = int(input())
f([], set(range(n)))