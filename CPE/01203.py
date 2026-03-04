def main():
    from sys import stdin
    e = stdin.readline

    import heapq
    pq = []

    while True:
        while True:
            s = e()
            if not s: return
            if s.strip() == '#': break
            r, arg, p = s.split()
            heapq.heappush(pq, (int(p), int(arg), int(p)))
        
        for _ in range(int(e().strip())):
            t, arg, p = heapq.heappop(pq)
            print(arg)
            heapq.heappush(pq, (t+p, arg, p))

main()