# a , b, c 매개변수
def multiple(a , b, c):
    num = a*b*c
    return num

a = 2
b = 3
c = 4

# a , b, c 위치인자로 전달
result = multiple(a , b, c)
print(result)