n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

b = [(i[0]**2 + i[1]**2, i) for i in a]
b.sort(reverse=True)

print(b[1][1][0], b[1][1][1])