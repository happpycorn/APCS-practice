def main():
    from sys import stdin
    e = stdin.readline
    n = int(e())
    step = [e().split() for _ in range(n)]
    d = [("", 0) for _ in range(n+1)]

    for i in range(n):
        ver, action, content = step[i]
        ed_string, idx = d[int(ver)]

        if action == "[Insert]":
            ed_string = ed_string[:idx] + content + ed_string[idx:]
            idx += len(content)
        if action == "[Left]":
            idx = max(idx - int(content), 0)
        if action == "[Right]":
            idx = min(idx + int(content), len(ed_string))
        if action == "[Backspace]":
            nidx = idx - int(content)
            if nidx > -1:
                ed_string = ed_string[0:nidx] + ed_string[idx:len(ed_string)]
            else:
                ed_string = ed_string[idx:len(ed_string)]
            idx = max(nidx, 0)
        if action == "[Delete]":
            nidx = idx + int(content)
            if nidx < len(ed_string):
                ed_string = ed_string[0:idx] + ed_string[nidx:len(ed_string)]
            else:
                ed_string = ed_string[0:idx]
            idx = min(nidx, len(ed_string))
        if action == "[Print]":
            nidx = min(idx + int(content), len(ed_string))
            print(ed_string[idx:nidx])
        
        d[i+1] = (ed_string, idx)
main()