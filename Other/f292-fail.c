#include <stdio.h>
#include <stdlib.h>

#define N 100001

typedef struct Node {
    int number;
    struct Node* next;
} Node;


int parent[N];
Node* dir_hash[N];

int find(int idx) {
    if (parent[idx] == idx) return idx;
    return parent[idx] = find(parent[idx]);
}

signed main(void) {
    int n, m;
    scanf("%d %d", &n, &m);
    for (int i = 1; i <= n; i++) parent[i] = i;
    for (int i = 1; i <= n; i++) {
        Node* new_node = (Node*)malloc(sizeof(Node));
        new_node->number = i;
        new_node->next = NULL;
        dir_hash[i] = new_node;
    }

    for (int i = 0; i < m; i++) {
        int orp, p, q;
        scanf("%d", &orp);
        switch (orp) {
        case 1:
            scanf("%d %d", &p, &q);
            int idx = find(p);
            parent[q] = idx;
            Node* curr = dir_hash[p];
            Node* last;
            while (curr != NULL) {
                last = curr;
                curr = curr->next;
            }
            last->next = dir_hash[q];
            break;
        case 2:
            scanf("%d %d", &p, &q);
            int p_idx = find(p);
            int q_idx = find(q);
            parent[p] = q_idx;
            Node* curr = dir_hash[p_idx];
            Node* last;
            while (curr->number != p) {
                last = curr;
                curr = curr->next;
            }
            last->next = curr->next;
            curr->next = dir_hash[q];
            dir_hash[q] = curr;
            break;
        case 3:
            scanf("%d", &p);
            Node* curr = dir_hash[p];
            int count = 0;
            long long sum_value = 0;
            while (curr != NULL) {
                count++;
                sum_value += curr->number;
                curr = curr->next;
            }
            printf("%d %lld", count, sum_value);
            break;
        
        default:
            break;
        }
    }
    return 0;
}