def main():
    import sys
    data = sys.stdin.read().splitlines()
    idx, out = 0, []
    while idx < len(data):
        x = int(data[idx].strip())
        idx += 1
        coe = list(map(int, data[idx].split()))
        idx += 1
        coe.pop()  # 移除最後的 0
        n = len(coe)
        if x == 0:
            out.append(str(coe[-1] if n > 0 else 0))
            continue
        s = 0
        # 預計算 x 的最大冪次
        power = x ** (n - 1)
        for i in range(n):
            s += (n - i) * coe[i] * power
            power //= x
        out.append(str(s))
    sys.stdout.write("\n".join(out))
main()