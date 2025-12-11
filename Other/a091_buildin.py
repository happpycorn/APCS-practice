def main():
    import sys
    import heapq
    from collections import defaultdict

    input_data = sys.stdin.read().split()
    if not input_data: return

    iterator = iter(input_data)

    min_h = []
    max_h = []
    deleted = defaultdict(int)
    content = []

    for cmd in iterator:
        cmd = int(cmd)
        
        if cmd == 1:
            val = int(next(iterator))
            heapq.heappush(min_h, val)
            heapq.heappush(max_h, -val)
            deleted[val] += 1
            
        elif cmd == 2:
            found_val = None
            while max_h:
                top = -max_h[0] 
                if deleted[top] > 0:
                    heapq.heappop(max_h)
                    deleted[top] -= 1
                    found_val = top
                    break
                else: heapq.heappop(max_h)
            if found_val is not None: content.append(found_val)

        elif cmd == 3:
            found_val = None
            while min_h:
                top = min_h[0]
                if deleted[top] > 0:
                    heapq.heappop(min_h)
                    deleted[top] -= 1
                    found_val = top
                    break
                else: heapq.heappop(min_h)
            if found_val is not None: content.append(found_val)

    sys.stdout.write('\n'.join(map(str, content)) + '\n')

main()