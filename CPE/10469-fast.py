def main():
    from sys import stdin
    data = stdin.read().splitlines()
    def xor(i): return i[0]^i[1]
    content = [str(xor(tuple(map(int, i.split())))) for i in data]
    print("\n".join(content))
main()