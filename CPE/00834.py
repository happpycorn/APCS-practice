def main():
    from sys import stdin
    data = stdin.read().splitlines()
    def f1(i):
        a, b = i
        p = a%b
        return f"[{a//b};{f(b, a%b)}]"
    def f(a, b):
        if a%b == 0: return a//b
        return f"{a//b},{f(b, a%b)}"
    content = [f1(map(int, i.split())) for i in data]
    print("\n".join(map(str, content)))
main()