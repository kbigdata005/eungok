import argparse
import random 
class Lottery:
    def __init__(self , mymoney):
        self.mymoney = mymoney
    def game(self):
        betting_money = int(input('배팅금액을 입력하세요!!'))
        if self.mymoney < betting_money:
            print("No more game!!!")
            return
        
        else:
            choice = 1   
            while choice:
                if self.mymoney < betting_money:
                    print("No more game becaur u are 빈털털이!!!")
                    choice = 0
                else:
                    select_num = int(input("숫자를 고르세요"))
                    random_num = random.randint(1,6)
                    if select_num != random_num:
                        print(f'당신의 숫자는 {select_num} , 난수는 {random_num}')
                        print('게임에서 패배하셨습니다.')
                        self.mymoney = self.mymoney - betting_money
                        print(f'현재잔액 {self.mymoney}')
                        select_game = input('게임을 계속 진행하실려면 1를 중단하실려면 2입력하세요!')
                        if select_game =="1":
                            choice = 1
                        elif select_game =='2':
                            choice = 0
                            print("게임을 종료합니다.")
                    elif select_num == random_num:
                        print(f'당신의 숫자는 {select_num} , 난수는 {random_num}')
                        print('게임에서 승리하셨습니다.')
                        self.mymoney = self.mymoney + betting_money*10
                        print(f'현재잔액 {self.mymoney}')
                        select_game = input('게임을 계속 진행하실려면 1 를 중단하실려면 2 입력하세요!')
                        if select_game =="1":
                            choice = 1
                        elif select_game =='2':
                            choice = 0
                            print("게임을 종료합니다.")
                
                # if choice == 0: 
                #     break
            
def parsing_argument():
    parser = argparse.ArgumentParser(description="Sample for using argparse",
                                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument(
       '-c',
       '--chargMoney',
       metavar="number",
       type=int,
       nargs=1,
       help="assignment variables",
       default=0
    )

    args = parser.parse_args()
    print(args)
    return args

def main():
    args = parsing_argument()
    lottery = Lottery(args.chargMoney[0])
    lottery.game()

main()