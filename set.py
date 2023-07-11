s1 = set([1, 1,1,1,1,1,2, 3])
print(s1)

s2 = set("Hello World")
print(s2)

s3 = list("Hello World")
print(s3)

s4 = tuple("Hello World")
print(s4)

s5 = set(tuple(list(set("Hello World"))))
print(s5)

# 교집합, 합집합, 차집합 구하기
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합

s3  = s1 & s2
print(s3)

s4 = s1.intersection(s2)
print(s4)

# 합집합
s3  = s1 | s2
print(s3)

s4 = s1.union(s2)
print(s4)

#차집합

s3  = s1 -s2
print(s3)

s4 = s1.difference(s2)
print(s4)

# 값 1개 추가하기 - add
s1 = set([1, 2, 3])
s1.add(5)
print(s1)

# 값 여러 개 추가하기 - update
s1 = set([1, 2, 3])
s1.update([1,2,4, 5, 6])
print(s1)

# 특정 값 제거하기 - remove
s1 = set([1, 2, 3])
s1.remove(1)
print(s1)