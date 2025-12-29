#include <stdio.h>
#include <stdlib.h>

#define int long long
#define N 100001

typedef struct {
    int w, f, d;
} Obj;

Obj objs[N];

signed compare(const void *a, const void *b) {
    Obj *obj_a = (Obj *)a;
    Obj *obj_b = (Obj *)b;
    return obj_a->w*obj_b->f-obj_b->w*obj_a->f;
}

signed main(void) {
    int n;
    scanf("%lld", &n);
    for (int i = 0; i < n; i++) scanf("%lld", &objs[i].w);
    for (int i = 0; i < n; i++) scanf("%lld", &objs[i].f);
    
    qsort(objs, n, sizeof(Obj), compare);
    
    int sum_value = 0;
    int sum_weight = 0;
    for (int i = 0; i < n; i++) {
        sum_value += sum_weight*objs[i].f;
        sum_weight += objs[i].w;
    }
    
    printf("%lld\n", sum_value);

    return 0;
}