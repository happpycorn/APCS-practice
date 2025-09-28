#include <stdio.h>
#define int long long

signed main(void) {
    int n, m;
    scanf("%lld %lld", &n, &m);
    int d[n];
    for (int i = 0; i < n; i++) scanf("%lld", &d[i]);

    int prefix[n+1];
    prefix[0] = 0;
    for (int i = 0; i < n; i++) {
        prefix[i+1] = prefix[i] + d[i];
    }

    for (int j = 0; j < m; j ++){

        int s, e;
        scanf("%lld %lld", &s, &e);

        int sum = prefix[e+1] - prefix[s];

        // int sum = 0;
        // for (int i = s; i < e; i++) sum += d[i];

        printf("%lld\n", sum);
    }
}