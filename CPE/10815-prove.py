def main():
    from sys import stdin
    from itertools import groupby
    print(*sorted(set("".join(map(str.lower, word))
                      for line in stdin
                      for isalpha, word in groupby(line, key=str.isalpha)
                      if isalpha)), sep="\n")
main()