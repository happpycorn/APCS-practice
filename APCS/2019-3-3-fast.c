#include <stdio.h>

#define int long long

int luckNumber(int l, int r, int d[], int idx[]) {
    if (l+1 == r) return d[r]-d[l];

    static int n_i = 1;
    while (1) {
        printf("%lld, %lld, %lld\n", l, r, idx[n_i]);
        if (l <= idx[n_i] && idx[n_i] < r) break;
        n_i++;
    }

    int m = idx[n_i];

    if (d[m]-d[l] > d[r]-d[m+1]) return luckNumber(l, m, d, idx);
    else return luckNumber(m+1, r, d, idx);
}

signed main(void) {
    int n;
    scanf("%lld", &n);

    int d[n+1], idx[n+1], value;
    d[0] = 0;
    for (int i = 0; i < n; i++) {
        scanf("%lld", &value);
        d[i+1] = d[i] + value;
        idx[value] = i;
    }

    for (int i = 0; i < n; i++) printf("%lld ", idx[i+1]);
    printf("\n");

    printf("%lld\n", luckNumber(0, n, d, idx));
    return 0;
}
