def main():
    from sys import stdin
    data = stdin.read().splitlines()
    index = 0
    n, m = map(int, data[index].split())
    index += 1
    p = list(map(int, data[index].split()))
    index += 1
    q = map(int, data[index].split())
    
    d = [0]*(2*n+1)
    for i in range(n*2):
        d[i] = d[i-1] + p[i%n]

    pos = 0
    for i in q:
        left = 0
        right = n-1
        while left <= right:
            mid = (left+right)//2
            if d[mid+pos] - d[pos-1] >= i:
                npos = mid
                right = mid - 1
            else:
                left = mid + 1
        pos = (pos + npos + 1)%n

    print(pos)

main()