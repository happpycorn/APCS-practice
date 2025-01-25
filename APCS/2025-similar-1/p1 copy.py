a, _, s = map(int, input().split())
m = list(map(int, input().split()))
d = map(int, input().split())

m_n = [0]*a
sum_value = 0
for i in range(a-1):
    sum_value += m[i]
    m_n[i+1] = sum_value

sum_value = 0

for i in d:
    if i > s: sum_value += m_n[s-1] - m_n[i-1]
    if i < s: sum_value += m_n[i-1] - m_n[s-1]
    s = i

print(sum_value*-1)