def main():
    a = int(input())
    def f(l):
        if len(l) == 1: return [l]
        d = []
        for i in range(len(l)):
            g = l[0:i] + l[i+1:len(l)]
            for j in f(g): d.append([l[i]] + j)
        return d
    content = [
        " ".join(map(str, i))
        for i in f(list(range(1, a+1)))
    ]
    print("\n".join(content))
main()