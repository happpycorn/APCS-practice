k = list(input())
n = int(input())
s = input()
d = set([s[i:i+n] for i in range(len(s)-n+1)])

find = False
words = []

def find_words(char, deep):
    global find
    if find: return
    if deep == n:
        words.append(char)
        if not char in d: 
            print(char)
            find = True
        return
    for w in k: find_words(char+w, deep+1)

find_words("", 0)