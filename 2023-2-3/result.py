record = input()

def read(index, start_pos, loop):

    movement = 0
    pos_record = []
    loop_record = []

    while index < len(record):

        if record[index] == "T":
            pos_record.append(int(record[index+1:index+3]))
            index += 3
        
        elif record[index] == "L":
            sp = start_pos if len(pos_record) == 0 else pos_record[-1]
            m, index, lp = read(index+2, sp, int(record[index+1]))
            pos_record.append(lp)
            loop_record.append(len(pos_record)-1)
            movement += m

        elif record[index] == "E":
            index += 1
            break
    
    pos = pos_record[0]
    for i, j in enumerate(pos_record):
        if i in loop_record:
            pos = j
            continue
        movement += abs(pos-j)
        pos = j
    
    movement = movement*loop + abs(pos_record[-1]-pos_record[0])*(loop-1) + abs(start_pos-pos_record[0])

    return movement, index, pos_record[-1]

print(read(0, 10, 1)[0])