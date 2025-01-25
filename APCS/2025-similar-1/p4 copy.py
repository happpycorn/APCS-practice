# 讀取輸入
n, m, k, p = map(int, input().split())

# 初始化數據結構
m_dict = {i+1: [{}, {}] for i in range(m + n)}  # 每個節點包含 [來的邊, 去的邊]
await_list = []

# 讀取邊的關係並初始化
for _ in range(k):
    start, end = map(int, input().split())
    m_dict[end][0][start] = 1  # end 的 incoming
    m_dict[start][1][end] = 1  # start 的 outgoing
    await_list.append([start, end])

# 傳播最短路徑的資訊
while await_list:
    start, end = await_list.pop(0)

    # 更新 start 的 outgoing 節點資訊，基於 end 的 outgoing
    for key, value in m_dict[end][1].items():
        new_distance = value + 1
        if key not in m_dict[start][1] or new_distance < m_dict[start][1][key]:
            m_dict[start][1][key] = new_distance
            await_list.append([start, key])

    # 更新 end 的 incoming 節點資訊，基於 start 的 incoming
    for key in m_dict[start][0].keys():
        if key not in m_dict[end][0]:
            await_list.append([key, start])

# 計算結果
result = [float("inf")] * m
for node, (incoming, outgoing) in m_dict.items():
    # 篩選只考慮來自 1~n 的 incoming
    incoming_from_n = {k: v for k, v in incoming.items() if k <= n}
    if not incoming_from_n:
        continue

    # 計算最小環狀距離
    min_coming_value = min(min(abs(p - i), n - abs(p - i)) for i in incoming_from_n)

    # 更新 result，針對 outgoing 到虛擬節點 (n+1 ~ n+m)
    for target, dist in outgoing.items():
        if target > n:
            result[target - n - 1] = min(result[target - n - 1], dist + min_coming_value + 1)

# 輸出結果
for res in result:
    print(res if res != float("inf") else -1)
