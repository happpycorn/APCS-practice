a = int(input())
b = [int(_) for _ in input().split()]
w = [int(_) for _ in input().split()]

d = b[2:4]

k = sum(d) #

m, o = [x**2 for x in b[0:2]]

f = m * b[2]
g = o * b[3]

h = g + f #小杯子體積+大杯子體積

c2,c3 =[],[]

for item in w:
    if f - item < 0:

        if h - item < 0:
            print(int(k))
            break

        elif h - item > 0:
            j = h - item
            h1 = j / o      # 剩餘高
            h2 = k - h1     # 水高

            c2.append(h2)
            c2.sort()
            print(int(c2[-1]))

    else: #f - item >= 0:
        j2 = f - item
        h3 = j2 / m         # 高
        h4 = k-h3-d[1]      # 水高

        c3.append(h4)
        c3.sort()
        print(int(c3[-1]))
        break