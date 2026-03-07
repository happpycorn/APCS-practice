def main():
    from sys import stdin
    e = stdin.readline
    n, m = map(int, e().split())
    d = [list(map(int, e().split())) for _ in range(n)]
    dp = [[0]*m for _ in range(n)]
    num = 0
    max_size = 0
    direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for i in range(n):
        for j in range(m):
            if d[i][j] != 1: continue

            num += 1
            d[i][j] = -1
            stack = [(i, j)]
            idx = 0
            size = 0

            while idx < len(stack):
                for dx, dy in direct:
                    x = stack[idx][0] + dx
                    y = stack[idx][1] + dy
                    if not(-1 < x < n and -1 < y < m): continue
                    if d[x][y] == 1:
                        stack.append((x, y))
                        d[x][y] = -1
                size += 1
                idx += 1
            
            if size > max_size: max_size = size

    print(num)
    print(max_size)
main()