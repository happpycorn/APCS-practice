int d[] = {1, 2, 3, 4}; // 一個長度為 n 的陣列
int n = sizeof(d) / sizeof(d[0]); // 計算陣列長度
int s = 0;
int q[n + 1]; // 定義一個長度為 n+1 的陣列 q
q[0] = 0;

for (int i = 0; i < n; ++i) {
    s += d[i];
    q[i + 1] = s;
}

int f(int i, int j) {
    return q[j] - q[i];
}