n, q = [int(i) for i in input().split()]

data = [int(i) for i in input().split()]

quest = [int(input()) for _ in range(q)]

for a in quest:

    isNotFind = True

    for i in range(len(data)):

        for j in range(len(data)-i-1):

            if abs(data[i] - data[j+1]) == a:

                isNotFind = False

                print("YES")

                break

            if not isNotFind:

                break
    
    if isNotFind:

        print("NO")