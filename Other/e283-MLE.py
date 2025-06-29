def main():
    from sys import stdin
    data = stdin.read().splitlines()
    index = 0
    content = []
    text_code = {
        "0 1 0 1" : "A",
        "0 1 1 1" : "B",
        "0 0 1 0" : "C",
        "1 1 0 1" : "D",
        "1 0 0 0" : "E",
        "1 1 0 0" : "F"
    }
    while index < len(data):
        n = int(data[index])
        index += 1
        text = [text_code[data[index+i]] for i in range(n)]
        content.append("".join(text))
        index += n
    print("\n".join(content))
main()