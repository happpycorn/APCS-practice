input()

a = []

a = [int(i) for i in input().split()]

a.sort()

w = "best case"

b = "worst case"

for i in a:

    if i < 60:
        w = i
    else:
        b = i
        break
            

print(" ".join(map(str, a)))
print(w)
print(b)