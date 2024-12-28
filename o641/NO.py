n, k, m = map(int, input().split())

if m >= n : print(0)

else :

    f = list(map(int, input().split()))

    h = [f[m:]]

    new_data = h[0][:]

    for i in range(k) : # 最多 10^9 次

        for j in range(1, n-m) :  # 最多 10^5 * 10^9 = 10^14 次

            new_data[j-1] = h[i][j-1] ^ h[i][j]

        new_data[-1] = h[i][-1]

        if new_data in h : break
        else : h.append(new_data[:])

    print(h[k%len(h)][0])