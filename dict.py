a = {"a" : 1, "b":2}
print(a)
# immutable 예
a1 = {1: 5, 2: 3}   # int 사용
print(a1)
{1: 5, 2: 3}
a2 = {(1,5): 5, (3,3): 3} # tuple사용
print(a2)
{(1, 5): 5, (3, 3): 3}
a3 = { 3.6: 5, "abc": 3} # float 사용
print(a3)
{3.6: 5, 'abc': 3}
a4 = { True: 5, "abc": 3} # bool 사용
print(a4)
{True: 5, 'abc': 3}

print({"a" : 1, "a":2})


print(a2[(1,5)])

# keys() , values() , items()
print(a.keys())
print(a.values())
print(a.items())


# 새로운 키와 값을 아래와 같이 추가할 수 있습니다.
d = {'abc' : 1, 'def' : 2}
d['키값'] = 10
print(d)

#dict 만들기

# result = dict([('a', 1), ('b', 2), ("c", 3)])
# print(result)

newdict = dict( alice = 5, bob = 20, tony= 15, suzy = 30)
print(newdict)
{'alice': 5, 'bob': 20, 'tony': 15, 'suzy': 30}

# dictionary(딕셔너리) 변환
name_and_ages = [['alice', 5], ['Bob', 13]]
print(dict(name_and_ages))
{'alice': 5, 'Bob': 13}
name_and_ages = [('alice', 5), ('Bob', 13)]
print(dict(name_and_ages))
{'alice': 5, 'Bob': 13}
name_and_ages = (('alice', 5), ('Bob', 13))
print(dict(name_and_ages))
{'alice': 5, 'Bob': 13}
name_and_ages = (['alice', 5], ['Bob', 13])
print(dict(name_and_ages))
{'alice': 5, 'Bob': 13}

# 여러값 수정은 update 메소드를 사용합니다. 키가 없는 값이면 추가됩니다.
a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
a.update({'bob':99, 'tony':99, 'kim': 30})
print(a)


# dictionary(딕셔너리) for문
# for문을 통해 딕셔너리를 for문을 돌리면 key값이 할당됩니다.
# a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
# for i in a:
#     print(i)

# value값으로 for문을 반복하기 위해서는 values() 를 사용해야합니다.

# a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
# for i in a.values():
#     print(i)

# key와 value를 한꺼번에 for문을 반복하려면 items() 를 사용
a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
for i in a.items():
    print(i)

key_list=[]
value_list=[]
for key , value in a.items():
    key_list.append(key)
    value_list.append(value)
  
print(key_list)
print(value_list)

