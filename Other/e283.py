def main():
    from sys import stdin
    e = stdin.readline
    content = []
    text_code = {
        "0 1 0 1" : "A",
        "0 1 1 1" : "B",
        "0 0 1 0" : "C",
        "1 1 0 1" : "D",
        "1 0 0 0" : "E",
        "1 1 0 0" : "F"
    }
    while True:
        d = e().strip()
        if not d: break
        text = [text_code[e().strip()] for i in range(int(d))]
        content.append("".join(text))
    print("\n".join(content))
main()