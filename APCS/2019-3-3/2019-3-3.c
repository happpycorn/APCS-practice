#include <stdio.h>
#include <limits.h>

int isLeftBigger(int l, int m, int r, long long d[]) {
    long long left_sum = d[m-1] - d[l];
    long long right_sum = d[r] - d[m+1];
    return left_sum > right_sum;
}

long long luckNumber(int l, int r, long long d[]) {
    if (l+1 == r) {
        long long ans = d[l+1]-d[l];
        return ans;
    }

    int min_index;
    int min_value = INT_MAX;

    for (int i = l; i < r; i++) {
        if (d[i+1]-d[i] < min_value) {
            min_index = i+1;
            min_value = d[i+1]-d[i];
        }
    }

    int m = min_index;

    printf("%d, %d, %d\n", l, r, m);

    if (isLeftBigger(l, m, r, d)) return luckNumber(l, m-1, d);
    else return luckNumber(m, r, d);
}

int main(void)
{
    int n;
    scanf("%d", &n);
    long long d[n+1];
    long long value;
    d[0] = 0;
    for (int i = 0; i < n; i++) {
        scanf("%lld", &value);
        d[i+1] = d[i] + value;
    }

    long long anser = luckNumber(0, n, d);

    printf("%lld\n", anser);

    return 0;
}
