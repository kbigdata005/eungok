def even_sum():
    num = 0
    for i in range(11):
        if i % 2 == 1:
            continue
        num = num + i
    print(f'0부터 10까지 짝수의 합: {num} 입니다.')


even_sum()