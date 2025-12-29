#include <stdio.h>
#include <stdlib.h>

#define N 100001

int id[N*2];
int parent[N*2];
int cnt[N*2];
long long sum[N*2];
int node_count = N;

int find(int idx) {
    if (parent[idx] == idx) return idx;
    return parent[idx] = find(parent[idx]);
}

signed main(void) {
    int n, m;
    while (scanf("%d %d", &n, &m) != EOF) {
        for (int i = 1; i <= n; i++) {
            id[i] = i;
            parent[i] = i;
            cnt[i] = 1;
            sum[i] = i;
        }

        for (int i = 0; i < m; i++) {
            int orp, p, q;
            scanf("%d", &orp);
            switch (orp) {
            case 1: {
                scanf("%d %d", &p, &q);
                int root_p = find(id[p]);
                int root_q = find(id[q]);
                if (root_p == root_q) break;
                parent[root_p] = root_q;
                cnt[root_q] += cnt[root_p];
                sum[root_q] += sum[root_p];
                break;
            }
            case 2: {
                scanf("%d %d", &p, &q);
                int root_p = find(id[p]);
                int root_q = find(id[q]);
                if (root_p == root_q) break;
                id[p] = node_count;
                parent[node_count] = root_q;
                node_count++;
                cnt[root_p] -= 1;
                sum[root_p] -= p;
                cnt[root_q] += 1;
                sum[root_q] += p;
                break;
            }        
            case 3:{
                scanf("%d", &p);
                int root_p = find(id[p]);
                printf("%d %lld\n", cnt[root_p], sum[root_p]);
                break;
            }
            default:
                break;
            }
        }
    }
    return 0;
}