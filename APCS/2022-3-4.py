def main():
    from sys import stdin
    from collections import deque
    e = stdin.readline
    n = int(e().strip())
    d = [list(map(int, e().split())) for _ in range(n)]

    direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(a, distance):
        wed = [[False]*n for _ in range(n)]
        q = deque([(0, 0)])
        wed [0][0] = True

        while len(q) > 0:
            x, y = q.popleft()
            for dx, dy in direct:
                nx, ny = dx + x, dy + y
                if not (-1 < nx < n and -1 < ny < n): continue
                if wed[nx][ny]: continue
                if abs(a[nx][ny] - a[x][y]) > distance: continue
                q.append((nx, ny))
                wed[nx][ny] = True
        
        return wed[n-1][n-1]
    
    def bsearch(a, l, r):
        ans = r
        while l <= r:
            mid = (l+r)//2
            if not bfs(a, mid): l = mid+1
            else: 
                ans = mid
                r = mid-1
        return ans
    
    def bfs_d(a, distance):
        wed = [[False]*n for _ in range(n)]
        q = deque([(0, 0, 0)])
        wed [0][0] = True

        while len(q) > 0:
            x, y, d = q.popleft()
            if x == n-1 and y == n-1: return d
            for dx, dy in direct:
                nx, ny = dx + x, dy + y
                if not (-1 < nx < n and -1 < ny < n): continue
                if wed[nx][ny]: continue
                if abs(a[nx][ny] - a[x][y]) > distance: continue
                q.append((nx, ny, d+1))
                wed[nx][ny] = True

    k = bsearch(d, 0, (max(max(d)) - min(min(d))))
    print(k)
    print(bfs_d(d, k))

main()