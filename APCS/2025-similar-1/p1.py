_, a, s = map(int, input().split())
m = list(map(int, input().split()))
d = map(int, input().split())

sum_value = 0

for i in d:
    if i > s: sum_value += sum(m[s-1:i-1])
    if i < s: sum_value += sum(m[i-1:s-1])
    s = i

print(sum_value)