str = "Hello"

for i in range(0, len(str)):
    print(f'{str[i]}_' , end="\n")


str_1= "Hello World"
str_1.upper
print(str_1.count("l"))


# 문자열 대문자로 변경하는 함수 (string.upper)
s1 = "rich"
s2 = s1.upper()
print(s2)

# 문자열 소문자로 변경하는 함수 (string.lower)

s1 = "RICH"
s2 = s1.lower()
print(s2)

# 문자가 대문자인지 확인하는 함수 (string.isupper)

s1 = "Rich"
s2 = s1.isupper()
print(s2)

# 문자가 소문자인지 확인하는 함수 (string.islower)

s1 = "rich"
s2 = s1.islower()
print(s2)

# 단어의 첫문자를 대문자로 바꿔주는 함수(string.title)

s1 = "rich"
s2 = s1.title()
print(s2)

# 대문자는 소문자로 소문자는 대문자로 (string.swapcase)

s1 = "RicH"
s2 = s1.swapcase()
print(s2)

# replace 특정단어를 다른 단어로 치화

a = "Hello World"

b = a.replace("Hello" , "Hi")
print(b)

# split 문자열 분리해서 리스트로 만들어 준다.
# str.split(sep=None, maxsplit=- 1)
c = a.split()
print(c)


# splitlines()
str ='''안녕하세요.
반갑습니다.
어서오세요~
'''
result = str.splitlines()
print(result)