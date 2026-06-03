def solve():
    import sys
    it = map(int, sys.stdin.read().split())

    next(it)
    w1 = next(it)
    w2 = next(it)
    h1 = next(it)
    h2 = next(it)

    v1 = w1 * w1 * h1
    max_v = v1 + w2 * w2 * h2
    
    inv_a1 = 1.0 / (w1 * w1)
    inv_a2 = 1.0 / (w2 * w2)
    
    max_h = h1 + h2

    curr_v = 0
    curr_h = 0.0
    max_inc = 0.0

    for cup in it:
        if curr_v >= max_v:
            break
            
        curr_v += cup
        
        if curr_v <= v1:
            nxt_h = curr_v * inv_a1
        elif curr_v <= max_v:
            nxt_h = h1 + (curr_v - v1) * inv_a2
        else:
            nxt_h = max_h
            
        inc = nxt_h - curr_h
        if inc > max_inc:
            max_inc = inc
            
        curr_h = nxt_h

    sys.stdout.write(str(int(max_inc + 1e-9)) + '\n')

solve()