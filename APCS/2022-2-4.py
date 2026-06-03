def main():
    from sys import stdin
    e = stdin.readline
    n, m = map(int, e().split())
    lst_a = list(map(int, e().split()))
    lst_b = list(map(int, e().split()))
    if len(lst_a) < len(lst_b):
        lst_a, lst_b = lst_b, lst_a
    lst_b.reverse()

    def kadane(lst):
        max_value = float("-inf")
        current_value = float("-inf")
        for i in lst:
            current_value = max(i, i+current_value)
            max_value = max(max_value, current_value)
        return max_value
    
    max_value = float("-inf")
    for i in range(len(lst_b)):
        max_value = max(max_value, kadane(
            [lst_a[j]*lst_b[len(lst_b)-i+j] for j in range(i)]
        ))
        max_value = max(max_value, kadane(
            [lst_a[len(lst_a)-i+j]*lst_b[j] for j in range(i)]
        ))

    for i in range(len(lst_a)-len(lst_b)+1):
        max_value = max(max_value, kadane(
            [lst_a[i+j]*lst_b[j] for j in range(len(lst_b))]
        ))

    lst_b.reverse()
    for i in range(len(lst_b)):
        max_value = max(max_value, kadane(
            [lst_a[j]*lst_b[len(lst_b)-i+j] for j in range(i)]
        ))
        max_value = max(max_value, kadane(
            [lst_a[len(lst_a)-i+j]*lst_b[j] for j in range(i)]
        ))

    for i in range(len(lst_a)-len(lst_b)+1):
        max_value = max(max_value, kadane(
            [lst_a[i+j]*lst_b[j] for j in range(len(lst_b))]
        ))
    
    print(max_value)
main()