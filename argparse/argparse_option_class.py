class Cat:
    def __init__(self , name , color , sound):
        self.name = name
        self.color = color
        self.sound = sound
    
    def __str__(self):
        return f'Cat(name={self.name} , color={self.color} , sound={self.sound})'
    
    def lotto(self):
        print(f'이름은 {self.name}이고 , 색깔은 {self.color}에 고양이가 , {self.sound}라고 웁니다.')



# nabi = Cat("나비" , "흰색")
# nero = Cat("네로" , "검은색")

# print(nabi)
# print(nero)