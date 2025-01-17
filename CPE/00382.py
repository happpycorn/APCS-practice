def main():
    from sys import stdin
    e = stdin.readline
    print("PERFECTION OUTPUT")
    while True:
        d = e().strip().split()
        if not d: break
        d = map(int, d)
        for i in d:
            if i == 0: print("END OF OUTPUT"); break
            if i == 1: print(f"{i:>5}  DEFICIENT"); continue
            sum_fac = 1
            for j in range(2, i):
                if i % j == 0: sum_fac += j
            if sum_fac > i: print(f"{i:>5}  ABUNDANT")
            elif sum_fac < i: print(f"{i:>5}  DEFICIENT")
            else: print(f"{i:>5}  PERFECT")
main()