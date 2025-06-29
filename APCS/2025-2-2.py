def main():
    from sys import stdin
    data = stdin.read().splitlines()
    index = 0
    m, n, k = map(int, data[index].split())
    index += 1
    d = [data[index+i] for i in range(m)]
    index += m
    nd = [0]*m
    score = 0
    for _ in range(k):
        act = list(map(int, data[index].split()))
        index += 1
        for i in range(m):
            nd[i] = [d[i][(j-act[i])%n] for j in range(n)]
        for i in range(n):
            count_dict = {}
            for j in range(m):
                if nd[j][i] in count_dict.keys():
                    count_dict[nd[j][i]] += 1
                else:
                    count_dict[nd[j][i]] = 1
            score += max(count_dict.values())
        d = nd.copy()
    print(score)
main()