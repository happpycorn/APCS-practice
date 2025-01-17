n, k, m = map(int, input().split())

if m >= n : print(0)

else :

    h = [list(map(int, input().split()))]

    new_data = h[0][:]

    for i in range(k) :

        for j in range(1, n) :

            new_data[j-1] = h[i][j-1] ^ h[i][j]

        new_data[-1] = h[i][-1]

        h.append(new_data[:])

    for row in h:
        print(row)