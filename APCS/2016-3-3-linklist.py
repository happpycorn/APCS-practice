def main():
    from sys import stdin
    from collections import deque
    data = stdin.read().splitlines()
    n, m, k = map(int, data[0].split())

    dq = deque(range(1, n + 1))  # 模擬 serive 列表
    for _ in range(k):
        dq.rotate(-(m - 1))  # 將要被淘汰的人轉到左端
        dq.popleft()         # 淘汰這個人

    print(dq[0])  # 剩下的第 pos 人
main()