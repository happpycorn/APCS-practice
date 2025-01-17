input()
w1, w2, h1, h2 = map(int, input().split())
cup = map(int, input().split())

fill1 = w1**2 * h1
fill2 = w2**2 * h2

maxRecord = 0

for i in cup:

    if i <= fill1:

        fill1 -= i
        maxRecord = max(i / w1**2, maxRecord)
    
    else:

        more = i - fill1
        fill1 = 0

        if more <= fill2:

            fill2 -= more
            maxRecord = max(((i-more) / w1**2) + (more / w2**2), maxRecord)

        else:

            maxRecord = max(((i-more) / w1**2) + h2, maxRecord)

print(int(maxRecord))