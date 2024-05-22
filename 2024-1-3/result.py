p, q, r, m = map(int, input().split())

input_result = list(map(int, input().split()))
result = [[0, i] for i in input_result]

result.extend([[None, None]] * q)

logic_gat = list(map(int, input().split()))

lines = [tuple(map(int, input().split())) for _ in range(m)]

logics = {
    1 : lambda x, y : x and y,
    2 : lambda x, y : x or y,
    3 : lambda x, y : (x or y) and not (x and y),
    4 : lambda x : not x
}

def decide(gat_number):

    global result

    load = []

    for i in lines:

        if i[1] == gat_number:


            if result[i[0]-1][0] is None:

                decide(i[0])

            load.append(result[i[0]-1])

            if len(load) > 1:

                break

    arg = [i[1] for i in load]

    depth = max([i[0] for i in load]) + 1

    logic = logics[logic_gat[gat_number-p-1]]

    result[gat_number-1] = [depth, int(logic(*arg))]

output_number = range(p + q + 1, p + q + r + 1)
input_number = [(i[1],i[0]) for i in lines if i[1] in output_number]
input_number.sort()
output_value = [None] * len(input_number)

for key, value in enumerate(input_number):

    if result[value[1]-1][0] is None:

        decide(value[1])
    
    output_value[key] = result[value[1]-1][1]

print(max(result, key=lambda x: x[0])[0])

print(" ".join(map(str, output_value)))