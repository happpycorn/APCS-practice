n, m = map(int, input().split())

record = [map(int, input().split()) for _ in range(n)]

ori_value = m
max_value = m

for result, score in record:

    ori_n = int((score - ori_value) * 0.05)
    max_n = int((score - max_value) * 0.05)

    if result :

        ori_r = max(1, ori_n + 25)
        max_r = max(1, max_n + 25)

        max_value += max_r
        ori_value += ori_r

    else :

        ori_r = min(0, ori_n - 25)
        ori_w = max(1, ori_n + 25)
        max_r = min(0, max_n - 25)

        max_value = max(ori_value + ori_w, max_value + max_r)
        ori_value += ori_r

print(max_value)