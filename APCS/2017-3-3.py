def main():
    from sys import stdin
    data = stdin.read().splitlines()
    index = 0
    n = int(data[index])
    index += 1

    in_deg = set(range(n))
    tree = {}
    for i in range(n):
        d = list(map(int, data[index].split()))
        index += 1
        tree[i] = [0]*d[0]
        for j in range(d[0]):
            tree[i][j] = d[j+1]-1
            in_deg.discard(d[j+1]-1)
    root = in_deg.pop()

    stack = [root]
    sum_h = [0]*n
    visited = [False]*n
    while stack:
        r = stack[-1]
        if visited[r]:
            stack.pop()
            max_h = 0
            for i in tree[r]:
                max_h = max(sum_h[i], max_h)
            sum_h[r] = max_h+1
        else:
            visited[r] = True
            for i in tree[r]:
                stack.append(i)
    print(f"{root+1}\n{sum(sum_h)-n}")
main()