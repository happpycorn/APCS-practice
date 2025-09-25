n = int(input())
d = []
pos = ["good", "best", "awesome", "excellent", "wonderful"]
neg = ["bad", "worst", "stupid", "shame"]
for _ in range(n):
    ss = input().translate(str.maketrans(".,:;?!'\"-", ' '*9)).lower().split()
    score = 0
    for s in ss:
        if s in pos: score += 1
        if s in neg: score -= 1
    d.append(str(score))
print(",".join(d))