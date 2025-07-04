def main():
    from sys import stdin
    e = stdin.readline
    e()
    a = list(map(int, e().strip().split(",")))
    b = list(map(int, e().strip().split(",")))
    ave_a = sum(a)/len(a)
    ave_b = sum(b)/len(b)
    if ave_a > ave_b: print(1)
    elif ave_a < ave_b: print(2)
    else: print(0)
main()