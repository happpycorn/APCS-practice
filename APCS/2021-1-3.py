def main():
    from sys import stdin
    data = stdin.read().splitlines()
    index = 0
    n, k = map(int, data[index].split())
    d = [0]*n
    index += 1
    for i in range(n):
        x, j = map(int, data[index].split())
        d[i] = (j, x)
        index += 1
    d.sort()
    stick = [(0, k)]
    spend = 0
    for i, pos in d:
        left = 0
        right = len(stick)
        while True:
            mid = (left+right)//2
            if stick[mid][0] > pos:
                right = mid - 1
            elif stick[mid][1] < pos:
                left = mid + 1
            else:
                spend += stick[mid][1] - stick[mid][0]
                stick[mid:mid+1] = [(stick[mid][0], pos), (pos, stick[mid][1])]
                break
    print(spend)
main()