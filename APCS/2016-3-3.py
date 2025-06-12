def main():
    from sys import stdin
    data = stdin.read().splitlines()
    index = 0
    n, m, k = map(int, data[index].split())
    serive = [i+1 for i in range(n)]
    pos = 0
    for i in range(k):
        boom = (pos+(m-1)%(n-i))%(n-i)
        serive.pop(boom)
        pos = boom%(n-i-1)
    print(serive[pos])
main()