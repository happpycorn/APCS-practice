p, q, r, m = map(int, input().split())

result = [None] * (p + q)
result[:p] = list(map(int, input().split()))[:]

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

    if result[gat_number - 1] is not None:

        return result[gat_number - 1]
    
    load = [(i[0], i[1]) for i in lines if i[1] == gat_number]

    arg = [decide(i[0]) for i in load]

    logic = logics[logic_gat[gat_number-p-1]]

    result[gat_number-1] = int(logic(*arg))

    return result[gat_number - 1]

for i in range(q):

    if result[i + p] is None:

        decide(i + p + 1)

end_start = p + q

def road(road_number : int) -> int:

    if road_number > end_start:

        return -1

    next_line = [i[1] for i in lines if i[0] == road_number]

    max_long_road = max(road(i) for i in next_line)

    return max_long_road + 1

max_depth = max(road(i) for i in range(1, p+1))

print(max_depth)

output_number = range(p + q + 1, p + q + r + 1)

input_number = [i[0] for i in lines if i[1] in output_number]

input_number.sort()

print(" ".join([str(result[i-1]) for i in input_number]))