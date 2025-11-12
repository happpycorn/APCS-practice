#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int valid_time(const char *t, int len) {
    if (len != 8) return 0;
    if (t[2] != ':' || t[5] != ':') return 0;

    for (int i = 0; i < 8; i++) {
        if (i == 2 || i == 5) continue;
        if (!isdigit((unsigned char)t[i])) return 0;
    }

    int h = (t[0]-'0')*10 + (t[1]-'0');
    int m = (t[3]-'0')*10 + (t[4]-'0');
    int s = (t[6]-'0')*10 + (t[7]-'0');

    if (h > 23 || m > 59 || s > 59) return 0;

    return 1;
}

int to_seconds(const char *t) {
    int h, m, s;
    sscanf(t, "%d:%d:%d", &h, &m, &s);
    return h*60*60+m*60+s;
}

signed main(void) {
    char *t1 = NULL, *t2 = NULL;
    size_t cap1 = 0, cap2 = 0;
    ssize_t len1, len2;

    len1 = getline(&t1, &cap1, stdin);
    if (len1 == -1) return 1;
    if (t1[len1 - 1] == '\n') t1[--len1] = '\0';  // len1-- 移掉 \n

    len2 = getline(&t2, &cap2, stdin);
    if (len2 == -1) return 1;
    if (t2[len2 - 1] == '\n') t2[--len2] = '\0';

    if (!valid_time(t1, len1) || !valid_time(t2, len2)) {
        printf("error\n");
        free(t1);
        free(t2);
        return 1;
    }

    int s1 = to_seconds(t1);
    int s2 = to_seconds(t2);

    printf("%d\n", abs(s1 - s2));

    free(t1);
    free(t2);

    return 0;
}