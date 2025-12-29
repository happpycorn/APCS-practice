#include <stdio.h>
#include <stdlib.h>

#define int long long
#define MAX 250000

typedef struct {
    int i, j, l;
} Edge;

Edge edges[MAX];

int parent[MAX];

signed compare(const void *a, const void *b) {
    Edge *edge_a = (Edge *)a;
    Edge *edge_b = (Edge *)b;
    return edge_a->l-edge_b->l;
}

int find(int i) {
    if (parent[i] == i) return i;
    return parent[i] = find(parent[i]);
}

signed main(void) {
    // read
    int n, k;
    scanf("%lld %lld", &n, &k);
    int edge_count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int t;
            scanf("%lld", &t);
            if (i < j) {
                edges[edge_count].i = i;
                edges[edge_count].j = j;
                edges[edge_count].l = t;
                edge_count++;
            }
        }
    }
    
    // init dsu
    for (int i = 0; i < n; i++) parent[i] = i;

    // sort
    qsort(edges, edge_count, sizeof(Edge), compare);

    int group_count = n;
    for (int i = 0; i < edge_count; i++) {
        int root_x = find(edges[i].i);
        int root_y = find(edges[i].j);
        if (root_x == root_y) continue;

        if (group_count > k) {
            parent[root_x] = root_y;
            group_count--;
        } else {
            printf("%lld\n", edges[i].l);
            break;
        }
    }    

    return 0;
}