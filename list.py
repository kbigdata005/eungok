# a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ('Life', 'is')]


a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]

a_list = a[3]
print(a_list)

print(a_list[1:2])
print(a[3][1:2])

# 리스트 더하기(+)

# 리스트의 값 수정하기
a = [1, 2, 3]

a[2] = 10
print(a)

# del 함수를 사용해 리스트 요소 삭제하기
del a[1]
print(a)

# 리스트 요소 제거 - remove
b = [1, 2, 3, 1, 2, 3]
b.remove(3)
print(b)

# 리스트 요소 끄집어 내서 삭제 - pop
c = [1, 2, "ㅁ"]
print(c.pop())

# 리스트에 요소 추가하기 - append
d = [1, 2, 3]
d.append(4)
print(d)

# 리스트에 요소 삽입 - insert
# insert(a, b)는 리스트의 a번째 위치에 b를 삽입하는 함수

a = [1, 2, 3]
a.insert(0,4)
print(4)

# extend( )
nums = [1, 2, 3]
# nums.extend([4])
nums.extend(['a','b'])
print(nums)

# sort(*, key=None, reverse=False)
# sorted(iterable, /, *, key=None, reverse=False)
a = ["b", "a"]
b = [5, 2, 3, 1, 4]
c = sorted(["b", "a" ,"c"] , reverse=True)
a.sort()
b.sort()
print(a)
print(b)
print(c)

# a.sort(reverse=True)
# d = sorted(b , reverse=True)
# print(a)
# b.sort(reverse=True)
# print(b)
# print(b)

# key
''' 정렬을 목적으로 하는 함수를 값으로 넣는다. lambda를 이용할 수 있다.
key 값을 기준으로 정렬되고 기본값은 오름차순이다'''

str_list = ['좋은하루','good_morning','굿모닝','niceday']
print(sorted(str_list, key=len))

# 리스트 뒤집기 - reverse

a = ['a', 'c', 'b']
f = [1,2,'a', 'c', 'b']
g = [1,2,3, 'a', 1, 3]
a.reverse()
print(a)
f.reverse()
print(f)
g.reverse()
print(g)

# count 함수
a = [1, 1, 1, 2, 3]
print(a.count(1))

# clear 함수

a = [1, 1, 1, 2, 3]
a.clear()
print(a)

a.append(5)
print(a)

a.extend([3,4])
print(a)

a.append([3,4])
print(a)

