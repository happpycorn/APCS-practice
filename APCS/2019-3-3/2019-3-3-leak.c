#include <stdio.h>
#define int long long

signed main(void) {
    int n;
    scanf("%lld", &n);
    int d[n];
    for (int i = 0; i < n; i++) {
        scanf("%lld", &d[i]);
        printf("%lld ", d[i]);
    }
    printf("\n");
    return 0;
}