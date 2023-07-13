import argparse
import math

def quadratic_equation_roots(a, b ,c):
    if b**2 - 4*a*c < 0:
      print(f'실근이 없습니다.')
    else:
      x = b**2 - 4*a*c
      x1 = (-b + math.sqrt(x)) /(2*a)
      x2 = (-b - math.sqrt(x)) /(2*a)

      if b**2 - 4*a*c ==0 :
         print(f'방정식의 해는 중근 {x1} 입니다.')
      else :
         print(f'x1={x1} or x2={x2}')

def parsing_argument():
  parser = argparse.ArgumentParser(description='Process some Arguments Parsing',
                                  formatter_class=argparse.ArgumentDefaultsHelpFormatter)
   
   # positional argments
  parser.add_argument(
      'title',
      metavar='문자열',
      type=str,
      help="write your message at positional argments"
  )

  parser.add_argument(
      'a',
      metavar='숫자',
      type=float,
      help="이차항의 계수를 정할 숫자"
  )

  parser.add_argument(
      'b',
      metavar='숫자',
      type=float,
      help="일차항의 계수를 정할 숫자"
  )

  parser.add_argument(
      'c',
      metavar='숫자',
      type=float,
      help="상수항항의 계수를 정할 숫자"
  )


  args = parser.parse_args()
  print(args)
  return args

def main():
  args = parsing_argument()
  print(f'{args.title}는 다음과 같습니다.')
  quadratic_equation_roots(args.a, args.b ,args.c)
   

main()