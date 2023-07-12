a = 3
b = 5
def local_variable():
    global a
    b = 4
    a = a+b
    print(a)

print(a)


def local_variable_error():
    print(b)

# local_variable_error()
# local_variable()

print([x*x for x in [1,2,3,4,5,6,7,8,9]])

