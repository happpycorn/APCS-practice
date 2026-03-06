def main():
    from sys import stdin
    input_data = stdin.read().split()
    if not input_data: return
    it = iter(input_data)
    content = []
    import heapq

    while True:
        if (n := next(it)) == '0': break
        pq = [int(next(it)) for _ in range(int(n))]
        heapq.heapify(pq)
        
        cost = 0
        while len(pq) > 1:
            c = heapq.heappop(pq) + heapq.heappop(pq)
            cost += c
            heapq.heappush(pq, c)
        
        content.append(cost)

    print("\n".join(map(str, content)))

main()