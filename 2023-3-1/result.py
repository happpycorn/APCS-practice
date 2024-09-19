pos, con = map(int,input().split())

mi = []
ma = []
eq = 0

for i in input().split():

    i = int(i)

    if i == eq:

        eq += 1
    
    elif i > pos:

        ma.append(i)
    
    else:

        mi.append(i)

if len(ma) > len(mi):

    print(len(ma)+eq, max(ma))

else:

    print(len(mi)+eq, min(mi))