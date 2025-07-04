def main():
    from sys import stdin
    e = stdin.readline
    n = int(e().strip())
    d = []
    pos = ["good", "best", "awesome", "excellent", "wonderful"]
    neg = ["bad", "worst", "stupid", "shame"]
    for _ in range(n):
        ss = e().strip().translate(str.maketrans(".,:;?!'\"-", ' '*9)).split()
        score = 0
        for s in ss:
            if s.lower() in pos: score += 1
            if s.lower() in neg: score -= 1
        d.append(str(score))
    print(",".join(d))
main()