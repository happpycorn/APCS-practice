def main():
    from sys import stdin
    e = stdin.readline

    # 先讀入所有操作
    n = int(e())
    o = tuple(e().strip() for _ in range(n))

    # 初始化歷史紀錄,記錄指標
    stk = [e().strip()]  # 將初始字串讀入
    idx = 0

    for e in o:
        if e.startswith("search"):
            _, s = e.split()
            print(stk[idx].count(s))
        elif e.startswith("replace"):
            _, s, r = e.split()
            if s == r: continue  # 被取代與取代字串相同就跳過 不創造新的紀錄
            idx += 1
            del stk[idx:]  # 將後面的紀錄都刪除
            stk.append(stk[-1].replace(s, r))
        elif e == "undo":
            if idx == 0:  # 沒有更前面的紀錄
                print("FAIL")
            else:
                idx -= 1
        elif e == "redo":
            if idx == len(stk) - 1:  # 沒有更後面的紀錄
                print("FAIL")
            else:
                idx += 1
        else:
            assert False
main()