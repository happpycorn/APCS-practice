def main():
    from sys import stdin
    e = stdin.readline
    case_count = 1
    while True:
        n = e().strip()
        if not n: break
        words_count = 0
        for _ in range(int(n)):
            word = e().strip()
            letter_count = {}
            for i in word:
                letter_count[i] = letter_count.get(i, 0) + 1
            if len(letter_count.values()) > 1 and len(letter_count.values()) == len(set(letter_count.values())): words_count += 1
        print(f"Case {case_count}: {words_count}")
        case_count += 1
main()