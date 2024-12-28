n, m = map(int, input().split())
d = [max(map(int, input().split())) for _ in range(n)]
sumd = sum(d)
pd = [i for i in d if sumd % i == 0]
print(sumd)
if len(pd) == 0: print(-1)
else: print(" ".join(map(str, pd)))