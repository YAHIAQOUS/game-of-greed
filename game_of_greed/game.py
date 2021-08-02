from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
                    
class Game:
    def __init__(self):
        self.roller =None
    
    def play(self,roller=None):
        self.roller=roller or GameLogic.roll_dice
        print('Welcome to Game of Greed')
        banker = Banker()
        round = 1
        loop = True

        user_input=input("(y)es to play or (n)o to decline\n> ")
        if user_input == 'n':
            print('OK. Maybe another time')

        elif user_input == 'y':
            while loop and banker.balance <= 10000:
                remainning_dice = 6
                while loop:
                    print(f'Starting round {round}\nRolling {remainning_dice} dice...')
                
                    rollDice= " ".join(str(item)for item in(self.roller(remainning_dice)))
                    # rollDice=(roller)
                    print(f"*** {rollDice} ***")

                    dice_input = input('Enter dice to keep, or (q)uit:\n> ')

                    if dice_input == "q":
                        print(f'Thanks for playing. You earned {banker.balance} points')
                        loop = False
                    else:
                        score = GameLogic.calculate_score(dice_input)
                        banker.shelf(score)
                        remainning_dice = remainning_dice - len(dice_input)
                        print(f'You have {banker.shelved} unbanked points and {remainning_dice} dice remaining')
                        user_choose = input("(r)oll again, (b)ank your points or (q)uit:\n> ")
                        if user_choose == "b":
                           
                            banker.bank()
                            print(f"You banked {score} points in round {round}\nTotal score is {banker.balance} points")
                            round=round+1
                            banker.clear_shelf()
                            break
                        elif user_choose == "q":
                            print("again",user_choose)
                            print(f"Thanks for playing. You earned {banker.balance} points")
                            loop = False
                        elif user_choose == "r":
                            continue


if __name__ == "__main__":
    playGmae = Game
    playGmae.play()       

