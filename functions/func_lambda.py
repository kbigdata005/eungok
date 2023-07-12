# 람다 표현식에 조건부 표현식 사용하기
'''
먼저 람다 표현식에서 조건부 표현식을 사용하는 방법을 알아보겠습니다.

lambda 매개변수들: 식1 if 조건식 else 식2
다음은 map을 사용하여 리스트 a에서 3의 배수를 문자열로 변환합니다.
'''

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_data = list(map(lambda x: str(x) if x % 3 == 0 else x, a))
print(list_data)

list_data_1 = list(map(lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10, a))
print(list_data_1)

# map에 객체를 여러 개 넣기
a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]

list_data_2 = list(map(lambda x, y: x * y, a, b))
print(list_data_2)


# filter 사용하기
a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
list_data_3 =list(filter(lambda x: x > 5 and x < 10, a))
print(list_data_3)


# reduce 사용하기
'''
reduce의 반환값이 15가 나왔습니다. 
함수 f에서 x + y를 반환하도록 만들었으므로 reduce는 그림과 
같이 요소 두 개를 계속 더하면서 결과를 누적합니다.
'''
a = [1, 2, 3, 4, 5]
from functools import reduce
list_data_4 =reduce(lambda x, y: x + y, a)
print(list_data_4)