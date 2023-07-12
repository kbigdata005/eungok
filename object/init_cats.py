class Cat:
    def __init__(self , name , color="흰색"):
        self.name = name
        self.color = color

    def meow(self , sound):
        print(f'내 이름은 {self.name} , 색깔은 {self.color} , {sound}')

nabi = Cat("나비")
nabi.meow("야옹~야옹~")
print(nabi)
nero = Cat("네로" , "검은색")
print(nero.name)
print(nero.color)

nero.name = "미미"
nero.color = "갈색"
nero.meow("어흥~~쩝쩝!!")