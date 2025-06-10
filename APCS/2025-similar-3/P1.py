def main():
    from sys import stdin
    data = stdin.read().splitlines()
    idx = 0
    content = []

    n = int(data[idx])
    idx += 1
    d = [[] for _ in range(5)]
    for i in range(n):
        i_d = list(map(int, data[idx].split()))
        idx += 1
        for j in range(5):
            d[j].append([i_d[j], i])

    level = [[0, 0, 0, 0, 0] for _ in range(n)]
    for i in range(5):
        d[i].sort(reverse=True)
        last = None
        for j in range(n):
            l = (j/n)*100
            if last and d[i][j][0] == last[0]:
                level[d[i][j][1]][0] += last[1]
                level[d[i][j][1]][1] += last[2]
                level[d[i][j][1]][2] += last[3]
                level[d[i][j][1]][3] += last[4]
                level[d[i][j][1]][4] += last[5]
            elif l < 5:
                last = [d[i][j][0], 1, 2, 0, 0, 0]
                level[d[i][j][1]][0] += last[1]
                level[d[i][j][1]][1] += last[2]
                level[d[i][j][1]][2] += last[3]
                level[d[i][j][1]][3] += last[4]
                level[d[i][j][1]][4] += last[5]
            elif l < 10:
                last = [d[i][j][0], 1, 1, 0, 0, 0]
                level[d[i][j][1]][0] += last[1]
                level[d[i][j][1]][1] += last[2]
                level[d[i][j][1]][2] += last[3]
                level[d[i][j][1]][3] += last[4]
                level[d[i][j][1]][4] += last[5]
            elif l < 20:
                last = [d[i][j][0], 1, 0, 0, 0, 0]
                level[d[i][j][1]][0] += last[1]
                level[d[i][j][1]][1] += last[2]
                level[d[i][j][1]][2] += last[3]
                level[d[i][j][1]][3] += last[4]
                level[d[i][j][1]][4] += last[5]
            elif l < 35:
                last = [d[i][j][0], 0, 0, 1, 2, 0]
                level[d[i][j][1]][0] += last[1]
                level[d[i][j][1]][1] += last[2]
                level[d[i][j][1]][2] += last[3]
                level[d[i][j][1]][3] += last[4]
                level[d[i][j][1]][4] += last[5]
            elif l < 50:
                last = [d[i][j][0], 0, 0, 1, 1, 0]
                level[d[i][j][1]][0] += last[1]
                level[d[i][j][1]][1] += last[2]
                level[d[i][j][1]][2] += last[3]
                level[d[i][j][1]][3] += last[4]
                level[d[i][j][1]][4] += last[5]
            elif l < 80:
                last = [d[i][j][0], 0, 0, 1, 0, 0]
                level[d[i][j][1]][0] += last[1]
                level[d[i][j][1]][1] += last[2]
                level[d[i][j][1]][2] += last[3]
                level[d[i][j][1]][3] += last[4]
                level[d[i][j][1]][4] += last[5]
            else:
                last = [d[i][j][0], 0, 0, 0, 0, 1]
                level[d[i][j][1]][0] += last[1]
                level[d[i][j][1]][1] += last[2]
                level[d[i][j][1]][2] += last[3]
                level[d[i][j][1]][3] += last[4]
                level[d[i][j][1]][4] += last[5]
    for i in range(n):
        s = ""
        if level[i][0] > 0:
            s += f"{level[i][0]}A"
        if level[i][1] > 0:
            s += f"{level[i][1]}+"
        if level[i][2] > 0:
            s += f"{level[i][2]}B"
        if level[i][3] > 0:
            s += f"{level[i][3]}+"
        if level[i][4] > 0:
            s += f"{level[i][4]}C"
        content.append(s)
    print("\n".join(content))
main()