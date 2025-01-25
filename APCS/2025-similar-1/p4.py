n, m, k, p = map(int, input().split())
m_dict = {}
await_list = []
for i in range(m+n): m_dict[i+1] = [{}, {}] # from, go
for _ in range(k):
    start, end = map(int, input().split())
    m_dict[end][0][start] = 1
    m_dict[start][1][end] = 1
    await_list.append([start, end])
for start, end in await_list:
    for key, value in m_dict[end][1].items():
        m_dict[start][1][key] = min(m_dict[start][1].get(key, float("inf")), value+1)
    for key in m_dict[start][0].keys():
        await_list.append([key, start])
result = [float("inf")]*m
for key, value in m_dict.items():
    if all(v > n for v in value[0].values()): continue
    min_coming_value = min([min(abs(p-i), n-abs(p-i)) for i in value[0].values() if i <= n])
    for key, value in value[1].items():
        result[key-n-1] = min(result[key-n-1], value+min_coming_value+1)
for i in result: print(i)