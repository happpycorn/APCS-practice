a = int(input())
b = [int(_) for _ in input().split()]
w = [int(_) for _ in input().split()]
c,d,m,o,f,g = [],[],[],[],[],[]

l = len(b)
n = 2
s = int(l/n)
e = [b[i:i + s] for i in range(0, l, s)]

c.extend(e[0]) #底面積
d.extend(e[1]) #高
k = sum(d) #

c = [x**2 for x in c]
r= [x*y for x, y in zip(c, d)] 

m.append(c[0])
o.append(c[1])
f.append(r[0]) #小杯子體積
g.append(r[1]) #大杯子體積

f = [int(_)for _ in f]
g = [int(_)for _ in g]

h =g[0]+f[0] #小杯子體積+大杯子體積
c2,c3 =[],[]
for item in w:
    if f[0] - item < 0:
        if h- item <0:
           print(int(k))
           print('*')
           break
        elif h-item >0:
           j=h-item
           h1=j/c[1] #剩餘高
           h2 =k-h1 #水高
           if h2 >= k/2:
               print(int(h2))
               print('**')
               break
           else:
               c2.append(h2)
               c2.sort()
               print(int(c2[-1]))
               print('***')

    else: #f[0] - item >= 0:
        j2 = f[0]-item
        h3 = j2/c[0]
        h4 = k-h3-d[1]
        if h4>=k/2:
            print(int(h4))
            print('****')
            break
        else:
            c3.append(h4)
            c3.sort()
            if c3 == []:
                break
            else:
                print(int(c3[-1]))
                print('*****')
                break