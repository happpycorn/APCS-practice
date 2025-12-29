#include <stdio.h>
#include <stdlib.h>

#define TABLE_SIZE 1000003

typedef struct Node {
    unsigned long long key;
    long long count;
    struct Node* next;
} Node;

Node* table[TABLE_SIZE] = {NULL};

int hash(unsigned long long key) {
    return (int)(key%TABLE_SIZE);
}

void insert(unsigned long long key) {
    int index = hash(key);
    Node* curr = table[index];

    while (curr != NULL) {
        if (curr->key == key) {
            curr->count++;
            return;
        }
        curr = curr->next;
    }

    Node* new_node = (Node*)malloc(sizeof(Node));
    new_node->key = key;
    new_node->count = 1;
    new_node->next = table[index];
    table[index] = new_node;
}

long long find_count(unsigned long long mask) {
    int h = hash(mask);
    Node* curr = table[h];
    while (curr) {
        if (curr->key == mask) return curr->count;
        curr = curr->next;
    }
    return 0;
}

int char_to_bit(char c) {
    if (c >= 'A' && c <= 'Z') return c - 'A';
    if (c >= 'a' && c <= 'l') return c - 'a' + 26;
    return -1;
}

signed main(void) {
    int m, n;
    scanf("%d %d", &m, &n);

    unsigned long long full_mask = (1ULL << m) - 1;
    char s[1005];

    for (long long i = 0; i < n; i++) {
        scanf("%s", s);
        unsigned long long current_mask = 0;
        for (int j = 0; s[j] != '\0'; j++) {
            current_mask |= (1ULL << char_to_bit(s[j]));
        }
        insert(current_mask);
    }

    long long total_pairs = 0;
    for (int i = 0; i < TABLE_SIZE; i++) {
        Node* curr = table[i];
        while (curr) {
            unsigned long long mask_a = curr->key;
            unsigned long long mask_b = full_mask ^ mask_a;

            total_pairs += curr->count * find_count(mask_b);
            curr = curr->next;
        }
    }

    printf("%lld\n", total_pairs / 2);
    return 0;
}