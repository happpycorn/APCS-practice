def main():
    from sys import stdin, stdout
    e = stdin.read().splitlines()
    t = int(e[0])
    d = []
    r = []
    for i in range(1, t+1):
        c = e[i].split()
        if c[0] == "Sleep": d.append(c[1])
        if c[0] == "Kick" and d: d.pop()
        if c[0] == "Test": r.append(d[-1] if d else "Not in a dream")
    stdout.write("\n".join(r) + "\n")
main()