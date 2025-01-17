n = int(input())

data = []

for _ in range(n):

    name, classNumber, number, describe = input().split()
    classNumber = int(classNumber)
    number = int(number)

    data.append([classNumber, number, name, describe])

data.sort(key=lambda x : x[1])
data.sort(key=lambda x : x[0])

for i in data:

    print(i[0], i[1], i[2])
    print(i[3])