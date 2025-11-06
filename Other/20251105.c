#include <stdio.h>

int query(char s) {
    switch (s) {
    case 'I': return 1;
    case 'V': return 5;
    case 'X': return 10;
    case 'L': return 50;
    case 'C': return 100;
    case 'D': return 500;
    case 'M': return 1000;
    default: return -1;
    }
}

signed main(void) {
    int n;
    if (scanf("%d", &n) != 1) {
        printf("Error\n");
        return 1;
    }
    getchar();
    int d[n];
    for (int i = 0; i < n; i++) {
        int c = getchar();
        d[i] = query((char)c);
        if (d[i] == -1) {
            printf("Error\n");
            return 1;
        }
    }

    int sum_value = 0;
    for (int i = 0; i < n-1; i++) {
        int f = d[i];
        int s = d[i+1];

        sum_value += f < s ? f-s : f+s;
    }

    printf("%d\n", sum_value);

    return 0;
}