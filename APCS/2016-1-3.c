#include <stdio.h>
#include <stdlib.h>
#define int long long
#define N 10001

int s[N];
int e[N];

signed compare(const void *a, const void *b) {
    int *v_a = (int *)a;
    int *v_b = (int *)b;
    return (*v_a - *v_b);
}

signed main(void) {
    int n;
    scanf("%lld", &n);
    for (int i = 0; i < n; i++) 
        scanf("%lld %lld", &s[i], &e[i]);
    
    qsort(s, n, sizeof(int), compare);
    qsort(e, n, sizeof(int), compare);

    int p_s = 0, p_e = 0;
    int last = -1;
    int sum_value = 0;
    int layer = 0;
    while (p_e < n) {
        int cur_e = e[p_e];
        if (p_s >= n) {
            if (layer > 0) sum_value += cur_e - last;
            layer--;
            last = cur_e;
            p_e++;
            continue;
        }
        int cur_s = s[p_s];
        if (cur_s < cur_e) {
            if (layer > 0) sum_value += cur_s - last;
            layer++;
            last = cur_s;
            p_s++;
        } else {
            if (layer > 0) sum_value += cur_e - last;
            layer--;
            last = cur_e;
            p_e++;
        }
    }
    printf("%lld\n", sum_value);
    
    return 0;
}