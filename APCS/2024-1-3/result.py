p, q, r, m = [int(i) for i in input().split()]

result = [[-1, -1]] + [[0, int(i)] for i in input().split()] + [[-1, -1]] * q

logic_gat = [0] + [int(i) for i in input().split()]

lines = [[] for _ in range(q+r+1)]

for _ in range(m):

    value, key = [int(i) for i in input().split()]

    lines[key - p].append(value)

logics = {
    1 : lambda x, y : x and y,
    2 : lambda x, y : x or y,
    3 : lambda x, y : (x or y) and not (x and y),
    4 : lambda x : not x
}

def decide(gat_number):

    global result

    logic_function = logics[logic_gat[gat_number-p]]
    input_index = lines[gat_number - p]

    for i in input_index:

        if result[i][0] < 0:
            decide(i)
        
    inputs = [result[i] for i in input_index]

    depth = max([i[0] for i in inputs]) + 1

    arg = [i[1] for i in inputs]
    result[gat_number] = [depth, int(logic_function(*arg))]

output_index = range(q + 1, q + r + 1)
input_number = [lines[i][0] for i in output_index]
output_value = [-1] * len(input_number)

for key, value in enumerate(input_number):

    if result[value][0] < 0:
        decide(value)
    
    output_value[key] = result[value][1]

print(max(result, key=lambda x: x[0])[0])
print(" ".join(map(str, output_value)))