import random

# 生成测试数据函数
def generate_test_cases(num_cases):
    test_cases = []
    
    for _ in range(num_cases):
        N = random.randint(1, 50)  # N 取值范围 [1, 50]
        M = random.randint(1, 50)  # M 取值范围 [1, 50]
        values = [random.randint(-50, 50) for _ in range(N + M)]  # 生成 N + M 个整数，范围 [-50, 50]
        
        test_cases.append(f"{N} {M}")
        test_cases.append(" ".join(map(str, values)))  # 转换为字符串并合并
        
    return test_cases

# 生成最多 110 组测试数据
num_cases = 110
test_data = generate_test_cases(num_cases)

# 格式化为多行文本
test_data_str = "\n".join(test_data)

print(test_data_str)
