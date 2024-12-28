record = input()
idx = 0
mr = [[]]
lpr = []
def moveCount(mr, lpt):
    movement = 0
    start = pos = -1
    for i in mr:
        if i[0] == "T":
            if start == -1: start = i[1]
            else: movement += abs(pos-i[1])
            pos = i[1]
        if i[0] == "L":
            if start == -1: start = pos = i[1]
            movement += abs(pos-i[1]) + i[2]
            pos = i[3]
    movement = movement*lpt + abs(start-pos)*(lpt-1)
    print(start, movement, pos)
    return start, movement, pos
while idx < len(record):
    if record[idx] == "T":
        mr[-1].append(["T", int(record[idx+1:idx+3])])
        idx += 3
    elif record[idx] == "L":
        lpr.append(int(record[idx+1]))
        mr.append([])
        idx += 2
    elif record[idx] == "E":
        s, m, p = moveCount(mr.pop(), lpr.pop())
        mr[-1].append(["L", s, m, p])
        idx += 1
s, m, p = moveCount(mr.pop(), 1)
print(m)