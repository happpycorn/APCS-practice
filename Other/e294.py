def main():
    from sys import stdin
    data = stdin.read().splitlines()
    index = 0
    content = []
    while index < len(data):
        d = data[index]
        l = len(d)
        for i in range(l):
            digit = int(d[i])
            if digit % 2 == 0:
                mid = int(d[i:])
                num_digits = l - i - 1
                top = int(str(digit + 1) + "1" * num_digits)
                if digit > 0: bot = int(str(digit - 1) + "9" * num_digits)
                else:
                    if d[0] == "1" and i == 1:
                        bot = -1
                    else:
                        content.append(top - mid)
                        break
                content.append(min(top - mid, mid - bot))
                break
        else:
            content.append(0)
        index += 1
    print("\n".join(map(str, content)))
main()