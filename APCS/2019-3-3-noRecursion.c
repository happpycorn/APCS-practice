#include <stdio.h>
#include <limits.h>

#define int long long

signed main(void) {
    int n;
    scanf("%lld", &n);

    int prefix[n+1], idxsort[n+1], value;
    prefix[0] = 0;
    for (int i = 0; i < n; i++) {
        scanf("%lld", &value);
        prefix[i+1] = prefix[i] + value;
        idxsort[value] = i;
    }

    int l = 0, r = n;

    for (int i = 1; i <= n; i++) {
        while (l > idxsort[i] || idxsort[i] > r) i++;
        
        int m = idxsort[i];

        if (prefix[m]-prefix[l] > prefix[r]-prefix[m+1]) r = m;
        else l = m+1;

        if (l+1 == r) break;

        // printf("%lld, %lld\n", l, r);
    }

    printf("%lld\n", prefix[r]-prefix[l]);
    return 0;
}
