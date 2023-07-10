a = 10 
b = "Hello"

print(type(a))
print(type(b))


a = True
print(type(a))


c = d = e = 10
x, y, z = 10, 3.14, "abc"
print(c , d, e)
print(x , y , z)


str = "안녕하세요!!! '김태경'"
str_literal = """
fwefwefwefwe 
fwefwefwe \n
fwefwefwe 
fwefwefwefweffewf
"""

print(str)
print(str_literal)


# 리터럴 표기 방법

name= "김태경"
literal_1 = "안녕하세요!!!" + "  " + name + " fewfew"
print(literal_1)

literal_2 = f"안녕하세요!!!   {name}  fewfew"
print(literal_2)

print(3 == 3.0)

print( 3 ==3 and 3>5)
print(3 ==3 & 3>5)


print( 3 ==3 or False)

print(not False)
print( ~ False)

print (not 3>5)