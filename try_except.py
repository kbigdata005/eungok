list_1 = []

numbers = list(range(10))

# try:
#     x = int(input('나눌 숫자를 입력하세요: '))
#     y = 10 / x
#     print(y)
# except:    # 예외가 발생했을 때 실행됨
#     print('0으로 나누면 안돼!! 안돼!!')


# try:
#     x = int(input('나눌 숫자를 입력하세요: '))
#     y = 10 / x
#     print(y)
# except Exception as e:    # 예외가 발생했을 때 실행됨
#     print(f'error : {e}')

# try:
#     x = input('나눌 숫자를 입력하세요: ')
#     y = 10 + x
#     print(y)
# except Exception as e:    # 예외가 발생했을 때 실행됨
#     print(f'error : {e}')


def main():
    try:
        print("1")
        print("2")
        prin("3")
        print("4")
    except NameError as e:
        print("예외 발생! main ", e.args)
        print(e.__traceback__)

main()