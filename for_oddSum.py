total_sum = 0
for num in range(1, 101):
    if num % 2 == 1:
        continue
    total_sum += num

print("짝수의 합:", total_sum)
