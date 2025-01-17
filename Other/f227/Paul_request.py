n = int(input())

grade = {}

for _ in range(n):

    name, classNumber, number, describe = input().split()
    classNumber = int(classNumber)
    number = int(number)

    if classNumber not in grade:
        
        grade[classNumber] = []
    
    grade[classNumber].append([number, name, describe])

for key in sorted(grade):

    for number, name, describe in sorted(grade[key]):

        print(key, number, name)
        print(describe)