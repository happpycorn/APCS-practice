n = int(input())

score = -1
error = 0

best_time = 0

for i in range(n):

    t, s = map(int, input().split())

    if s < 0 : error += 1

    if s > score : best_time = t ; score = s

print(max(score-n-error*2, 0), best_time)