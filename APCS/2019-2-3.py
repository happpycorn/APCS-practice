def main():
    from sys import stdin
    data = stdin.read().splitlines()
    index = 0
    def f(x): return 2*x-3
    def g(x, y): return 2*x+y-7
    def h(x, y, z): return 3*x-2*y+z

    d = data[index].split()

    stack = [0]
    order_code = set({"f", "g", "h"})

    while stack:
        s = stack[-1]
        if d[s] == "f":
            if d[s+1] in order_code:
                stack.append(s+1)
                continue
            d[s] = f(int(d.pop(s+1)))
            stack.pop()
        elif d[s] == "g":
            if d[s+1] in order_code:
                stack.append(s+1)
                continue
            if d[s+2] in order_code:
                stack.append(s+2)
                continue
            d[s] = g(int(d.pop(s+1)), int(d.pop(s+1)))
            stack.pop()
        elif d[s] == "h":
            if d[s+1] in order_code:
                stack.append(s+1)
                continue
            if d[s+2] in order_code:
                stack.append(s+2)
                continue
            if d[s+3] in order_code:
                stack.append(s+3)
                continue
            d[s] = h(int(d.pop(s+1)), int(d.pop(s+1)), int(d.pop(s+1)))
            stack.pop()
    
    print(d[0])
main()