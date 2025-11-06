def main():
    import sys
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    out = [str(int(a) ^ int(next(it))) for a in it]
    sys.stdout.write("\n".join(out))
main()