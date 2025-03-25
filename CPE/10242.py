def main():
    import sys
    def compute_coordinates():
        for line in sys.stdin:
            points = list(map(float, line.split()))
            spoints = set()
            for i in range(0, 8, 2):
                p = (points[i], points[i+1])
                if p in spoints: p3 = p
                else: spoints.add(p)
            spoints.remove(p3)
            p1, p2 = spoints
            x, y = p1[0] - (p3[0] - p2[0]), p1[1] - (p3[1] - p2[1])
            yield f"{x:.3f} {y:.3f}"
    sys.stdout.write("\n".join(compute_coordinates()))
main()