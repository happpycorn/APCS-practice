import timeit

# 測試字串
setup = """
s = '9876543201234567890123456789'
"""

# 原始版本（使用 pow(10, n9)）
original = '''
def f(s):
    l = len(s)
    for i in range(l):
        if s[i] in '02468':
            x = int(s[i])
            mid = int(s[i:])
            n9 = l - i - 1
            pow10 = pow(10, n9)
            ones = 0 if n9 == 0 else pow10 // 9
            top = (x + 1) * pow10 + ones
            if x:
                bot = (x - 1) * pow10 + (pow10 - 1)
                return str(min(top - mid, mid - bot))
            else:
                if s[0] == '1' and i == 1:
                    return str(min(top - mid, mid + 1))
                else:
                    return str(top - mid)
    return '0'
f(s)
'''

# 優化版本（預算 pow10 陣列）
optimized = '''
def f(s):
    l = len(s)
    pow10 = [1] * (l + 1)
    for i in range(1, l + 1):
        pow10[i] = pow10[i - 1] * 10
    for i in range(l):
        if s[i] in '02468':
            x = int(s[i])
            mid = int(s[i:])
            n9 = l - i - 1
            p10 = pow10[n9]
            ones = 0 if n9 == 0 else p10 // 9
            top = (x + 1) * p10 + ones
            if x:
                bot = (x - 1) * p10 + (p10 - 1)
                return str(min(top - mid, mid - bot))
            else:
                if s[0] == '1' and i == 1:
                    return str(min(top - mid, mid + 1))
                else:
                    return str(top - mid)
    return '0'
f(s)
'''

# 跑 100_000 次看差異
runs = 100_000
t_orig = timeit.timeit(original, setup=setup, number=runs)
t_opt = timeit.timeit(optimized, setup=setup, number=runs)

# 顯示結果
print(f"Original (pow)   : {t_orig:.6f} sec")
print(f"Optimized (arr)  : {t_opt:.6f} sec")
print(f"Faster version   : {'Optimized' if t_opt < t_orig else 'Original'} by {abs(t_opt - t_orig):.6f} sec")
