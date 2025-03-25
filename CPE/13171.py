def main():
    from sys import stdin, stdout
    input_iter = iter(stdin)
    next(input_iter)  # 跳過第一行
    content = []
    for line in input_iter:
        m, y, c, a = line.split()
        m, y, c = int(m), int(y), int(c)
        sm = sy = sc = 0
        for ch in a:
            if ch == 'M': sm += 1
            elif ch == 'Y': sy += 1
            elif ch == 'C': sc += 1
            elif ch == 'R': sm += 1; sy += 1
            elif ch == 'V': sm += 1; sc += 1
            elif ch == 'G': sy += 1; sc += 1
            elif ch == 'B': sm += 1; sy += 1; sc += 1
        if m < sm or y < sy or c < sc:content.append("NO")
        else: content.append(f"YES {m-sm} {y-sy} {c-sc}")
    stdout.write("\n".join(content))
main()