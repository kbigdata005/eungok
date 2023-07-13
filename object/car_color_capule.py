class Car:

  def __init__(self, name,price, color):
    self.__name = name
    self.__price = price
    if price <= 100000000:
      raise ValueError('차값이 1억보다 커야 합니다.')
    self.__color = color

  def __str__(self):
    return (f'Car(name={self.__name} ,가격={self.__price}, age = {self.__color})')

  @property
  def color(self):
    return self.__color

  @color.setter
  def setColor(self, color):
    if self.__color == "노랑":
      raise ValueError('노랑은 안돼요!')
    self.__color = color



car = Car("자전거",110000000 , "파랑")
print(car)
print("==================")
# cat.age = 11
car.setColor ="Black"
# print(cat)
print(car.color)