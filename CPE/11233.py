def main():
    from sys import stdin
    data = stdin.read().splitlines()
    content = []
    idx = 0
    consonant = {"a", "e", "i", "o", "u"}
    es_set = {"o", "s", "x", "ch", "sh"}
    n, m = map(int, data[idx].split())
    idx += 1
    irr_words = {k: v for k, v in (data[idx+i].split() for i in range(n))}
    idx += n
    for j in range(m):
        i = data[idx+j].strip()
        if i in irr_words:
            content.append(irr_words[i])
        elif i[-1] == "y" and not i[-2] in consonant:
            content.append(i[:-1]+"ies")
        elif i[-1] in es_set or i[-2:] in es_set:
            content.append(i+"es")
        else: content.append(i+"s")
    print("\n".join(content))
main()