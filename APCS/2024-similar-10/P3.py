n, m, r, c, k = [int(i) for i in input().split()]

space = [[0]*r for _ in range(c)]

relations = []

for _ in range(m):

    a, b, x, y = [int(i) for i in input().split()]

    for i in range(len(relations)):
        
        if a in relations[i] and b in relations[i]:

            break

        elif a in relations[i]:

            for j in range(i+1, len(relations)):

                if b in relations[j]:

                    relations[i] = relations[i] + relations.pop(j)
                
                break
                
            else:

                relations[i].append(b)

                break
        
        elif b in relations[i]:

            for j in range(i+1, len(relations)):

                if a in relations[j]:

                    relations[i] = relations[i] + relations.pop(j)

                    break
                
            else:

                relations[i].append(a)
                
                break
    
    else:

        relations.append([a, b])

print(1, len(relations), max(map(len, relations)))