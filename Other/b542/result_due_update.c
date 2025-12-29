#include <stdio.h>
#include <stdlib.h>
#define int long long

#define MAX_N 100001
int d[MAX_N];

int compare(const void *a, const void *b) {
    int num1 = *(int *)a;
    int num2 = *(int *)b;
    if (num1 < num2) return -1;
    if (num1 > num2) return 1;
    return 0;
}

signed main(void) {
    int n, q;
    scanf("%lld %lld", &n, &q);
    for (int i = 0; i < n; i++) scanf("%lld", &d[i]);

    // sort
    qsort(d, n, sizeof(int), compare);

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