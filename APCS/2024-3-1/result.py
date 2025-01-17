n = int(input())
w1, w2, h1, h2 = map(int, input().split())
cup = [int(i) for i in input().split()]

record = [0] * n
end = 0

for i in range(n):

    start = end
    end += cup[i]

    if end <= w1**2*h1:

        record[i] = (end - start) / w1**2

    elif 0 < end-w1**2*h1 <= w2**2*h2:

        if start <= w1**2*h1:

            record[i] = ((w1**2*h1 - start) / w1**2) + ((end - w1**2*h1) / w2**2)
        
        else:

            record[i] = (end - start) / w2**2
    
    else:

        if start <= w1**2*h1:

            record[i] = ((w1**2*h1 - start) / w1**2) + h2

        else:

            record[i] = ((w2**2*h2 - start) / w2**2)

print(int(max(record)))