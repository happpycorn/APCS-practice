from collections import deque

def main():
    # 讀取 n 和 k
    n, k = map(int, input().split())
    pre = [0] * (n + 1)
    dp = [0] * (n + 1)
    dq = deque()
    dq.append((0, 0))

    # 讀取數值並計算前綴和
    values = list(map(int, input().split()))
    for i in range(1, n + 1):
        pre[i] = values[i - 1] + pre[i - 1]

    for i in range(1, n + 1):

        # 移除超出窗口範圍的元素
        while dq and i - dq[0][0] > k:
            dq.popleft()

        # 更新 dp[i]
        dp[i] = pre[i] - dq[0][1]
        dp[i] = max(dp[i], dp[i - 1])

        # 準備插入新的元素到 deque
        pb = pre[i] - dp[i - 1]
        while dq and dq[-1][1] >= pb:
            dq.pop()
        dq.append((i, pb))

        print(dq, dp)

    # 輸出結果
    print(dp[n])

main()
