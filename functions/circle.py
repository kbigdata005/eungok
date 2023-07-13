import math
import numpy as np
def circle_square_round(a):
    square = a*a*math.pi
    round = 2*a*math.pi
    return square, round
# a = int(input("반지름의 길이를 적으세요."))
rr, dd =circle_square_round(3)
# print(f'square = {square}, round = {round}')
square, round =circle_square_round(3)
a = np.floor(rr)
b = np.floor(dd)
print(a,b )