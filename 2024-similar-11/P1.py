n = int(input())

args = [int(input()) for _ in range(n)]

data = [0] * 5

point = 0

for arg in args:

    if arg == 0 : print(data[point])

    if arg == 1 : data[point] += 1

    if arg == 2 : point = point + 1 if point < 4 else 0

    if arg == 3 : point = point - 1 if point > 0 else 4