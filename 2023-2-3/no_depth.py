record = input()

index = 0
pos_record = [[]]
lpr = []

while index < len(record):

    if record[index] == "T":
        pos_record[-1].append(["T", int(record[index+1:index+3])])
        index += 3
    
    elif record[index] == "L":
        lpr.append([10 if len(pos_record[-1]) == 0 else pos_record[-1][-1][1], int(record[index+1])])
        pos_record.append([])
        index += 2
    
    elif record[index] == "E":
        pr = pos_record.pop()
        sp, lop = lpr.pop()
        pos = pr[0][1]
        movement = 0

        for i in pr:
            if i[0] == "T": movement += abs(pos-i[1])
            elif i[0] == "L": movement += i[2]
            pos = i[1]
        
        movement = movement * lop + abs(pos-pr[0][1]) * (lop-1) + abs(pr[0][1]-sp)

        pos_record[-1].append(["L", pos, movement])
        index += 1

pos = 10
movement = 0

for i in pos_record[-1]:

    if i[0] == "T": movement += abs(pos-i[1])
    elif i[0] == "L": movement += i[2]
    pos = i[1]

print(movement)