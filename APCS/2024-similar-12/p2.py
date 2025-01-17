n, m, q = map(int, input().split())

methods = [0]*n

for i in range(n):
    info = list(map(int, input().split()))
    method = [input().split() for _ in range(3)]
    methods[i] = [info, method]

a = list(map(int, input().split()))

bag = [[a[i], a[i+1]] for i in range(int(a/2))]

steps = [list(map(int, input().split())) for _ in range(q)]

table = [None]*9

for step in steps:

    if type(step) is list and len(step) == 4: # put

        if step[1] > len(bag): continue
        if step[2] > bag[step[1]][1]: continue

        if table[step[3]] is None:
            table[step[3]] = [step[1], bag[step[1]][1]]
        elif table[step[3]][0] == step[1]:
            table[step[3]][0] += bag[step[1]][1]
        else:
            bag[table[step[3]][0]] += table[step[3]][1]
            table[step[3]] = [step[1], bag[step[1]][1]]

        bag[step[1]][1] -= step[2]
    
    elif type(step) is list and len(step) == 2: # return

        if table[step[1]] is None: continue

        bag[table[step[1]][0]] += table[step[1]][1]
        table[step[1]] = None

    elif step == "craft":
        pass

f_bag = [i[0], i[1] for i in bag]
print(" ".join(map(str, f_bag)))