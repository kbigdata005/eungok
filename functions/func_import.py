import func_kwargs
from func_args import 함수
from func_kwargs import *

from func_kwargs import name_hello_함수 as nh
import numpy  as np


# func_kwargs.name_hello_함수(a= "kim", b="park", c='lee')
data = 함수(1,5,6,4,3,100)
print(data)
# name_hello_함수(a= "kim", b="park", c='lee')
nh(a= "kim", b="park", c='lee')


# 상위경로 import 

import sys, os
print(os.path.dirname(__file__))
print(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
print(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import hello

file_path= "C:\apps\test"
sys.path.append(file_path)

str = "Hello"


list_1 = [1,2,3,4,5]
list_2 = [2,5,3,2,10]
a = np.array(list_1)

b = np.array(list_2)
print(list_1 + list_2)
# print(a+b)
print(type(str))
print(type(a))


def a():
    return "3"
b = a()
print(type(b))