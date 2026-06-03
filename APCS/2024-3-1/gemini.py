def main():
    from sys import stdin
    e = stdin.readline
    n = int(e())
    w1, w2, h1, h2 = map(int, e().split())
    cups = list(map(int, e().split()))

    v1 = (w1 ** 2) * h1
    v2 = (w2 ** 2) * h2
    max_v = v1 + v2

    def get_height(volume):
        if volume <= 0: return 0
        elif volume <= v1: return volume / (w1 ** 2)
        elif volume <= max_v: return h1 + ((volume - v1) / (w2 ** 2))
        else: return h1 + h2

    current_vol = 0
    max_increase = 0

    for cup in cups:
        h_start = get_height(current_vol)
        current_vol += cup
        h_end = get_height(current_vol)

        increase = h_end - h_start
        if increase > max_increase:
            max_increase = increase

    print(int(max_increase))

main()