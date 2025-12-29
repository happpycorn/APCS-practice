#include <stdio.h>
#define int long long

signed main(void) {
    int n, q;
    scanf("%lld %lld", &n, &q);
    int d[n];
    for (int i = 0; i < n; i++) scanf("%lld", &d[i]);

    // sort
    for (int i = 0; i < n; i++) {
        for (int j = 1; j < n-i; j++) {
            if (d[j-1] > d[j]) {
                int t = d[j];
                d[j] = d[j-1];
                d[j-1] = t;
            }
        }
    }

    // double pointer
    for (int i = 0; i < q; i++) {
        int target;
        scanf("%lld", &target);

        int l = 0, r = 0;
        int found = 0;
        while (r < n) {
            int diff = d[r] - d[l];
            if (diff == target) {
                found = 1;
                break;
            } 
            else if (diff < target) r++;
            else if (diff > target) l++;
            if (r == l) r++;
        }
        
        if (found) printf("YES\n");
        else printf("NO\n");
    }
}