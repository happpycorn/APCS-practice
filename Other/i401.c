#include <stdio.h>
#define int long long

#define MAX_N 250000
#define MAX_XY 60005
int d[2][MAX_XY][MAX_N][2];
int d_c[2][MAX_XY] = {0}

signed main(void) {
    int n;
    scanf("%lld", &n);
    for (int i = 0; i < n; i++) {
        int x, y, f;
        scanf("%lld %lld %lld", &x, &y, &f);
        y += 30000;

        int idx = d_c[0][x];
        d[0][x][idx][0] = y;
        d[0][x][idx][1] = f;
        while (idx > 0) {
            if (d[0][x][idx][0] < d[0][x][idx-1][0]) {
                int t[2];
                t[0] = d[0][x][idx][0];
                t[1] = d[0][x][idx][1];
                d[0][x][idx][0] = d[0][x][idx-1][0];
                d[0][x][idx][1] = d[0][x][idx-1][1];
                d[0][x][idx-1][0] = t[0];
                d[0][x][idx-1][1] = t[1];
            }
            idx--;
        }
        d_c[0][x]++;

        int idx = d_c[1][y];
        d[1][y][idx][0] = x;
        d[1][y][idx][1] = f;
        while (idx > 0) {
            if (d[1][y][idx][0] < d[1][y][idx-1][0]) {
                int t[2];
                t[0] = d[1][y][idx][0];
                t[1] = d[1][y][idx][1];
                d[1][y][idx][0] = d[1][y][idx-1][0];
                d[1][y][idx][1] = d[1][y][idx-1][1];
                d[1][y][idx-1][0] = t[0];
                d[1][y][idx-1][1] = t[1];
            }
            idx--;
        }
        d_c[1][y]++;
    }

    int x = 0, y = 30000, d = 0;

}