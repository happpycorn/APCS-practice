#include <stdio.h>
#include <stdlib.h>

#define int long long

int luckNumber(int l, int r, int d[], int idx[][2]) {
    if (l+1 == r) return d[r]-d[l];

    static int n_i = 0;
    while (1) {
        // printf("%lld, %lld, %lld, %lld\n", l, r, idx[n_i][0], idx[n_i][1]);
        if (l <= idx[n_i][1] && idx[n_i][1] < r) break;
        n_i++;
    }

    int m = idx[n_i][1];

    if (d[m]-d[l] > d[r]-d[m+1]) return luckNumber(l, m, d, idx);
    else return luckNumber(m+1, r, d, idx);
}

signed cmp(const void *a, const void *b) {
    int *pa = (int*)a;
    int *pb = (int*)b;
    return pa[0] - pb[0];
}

signed main(void) {
    int n;
    scanf("%lld", &n);

    int d[n+1], idx[n][2], value;
    d[0] = 0;
    for (int i = 0; i < n; i++) {
        scanf("%lld", &value);
        d[i+1] = d[i] + value;
        idx[i][0] = value;
        idx[i][1] = i;
    }

    qsort(idx, n, sizeof(idx[0]), cmp);

    // for (int i = 0; i < n; i++) printf("%lld, %lld\n", idx[i][0], idx[i][1]);

    printf("%lld\n", luckNumber(0, n, d, idx));
    return 0;
}

