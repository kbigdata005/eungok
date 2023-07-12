def odd_sum():
    num = 0
    for i in range(11):
        if i % 2 == 0:
            continue
        num = num + i
    
    return num
    print(f'0부터 10까지 ㅊㄴㅇㅊㄴㅇㅊ의 합: {num} 입니다.')


result = odd_sum()
# print(f'0부터 10까지 홀수의 합: {result} 입니다.')