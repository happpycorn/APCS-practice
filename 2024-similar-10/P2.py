n = int(input())
step = [input().split() for _ in range(n)]
word = input()

record = []
undoRecord = []

for action in step:

    if action[0] == "search":

        print(word.count(action[1]))
    
    elif action[0] == "replace":

        if action[1] == action[2]: continue

        undoRecord = []
        record.append(word)
        word = word.replace(action[1], action[2])
        
    elif action[0] == "undo":

        if record:

            undoRecord.append(word)
            word = record.pop()

        else: print('FAIL')
    
    elif action[0] == 'redo':

        if undoRecord:

            record.append(word)
            word = undoRecord.pop()

        else: print('FAIL')