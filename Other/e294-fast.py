def main():
    def f(s):
        l = len(s)
        for i in range(l):
            if s[i] in '02468':
                x = ord(s[i]) - 48
                mid = int(s[i:])
                n9 = l-i-1
                pow10 = pow(10, n9)
                top = (x + 1) * pow10 + pow10 // 9
                if x:
                    bot = (x - 1) * pow10 + (pow10 - 1)
                    return str(min(top - mid, mid - bot))
                else:
                    if s[0] == '1' and i == 1: return str(min(top - mid, mid+1))
                    else: return str(top - mid)
        return '0'
    import sys
    data = sys.stdin.read().splitlines()
    sys.stdout.write('\n'.join(map(f, data)) + '\n')
main()