from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
from abc import ABC

class Game:
    def __init__(self):
        self.roller =None

    @classmethod
    def play(self,roller=None):
        self.roller=roller or GameLogic.roll_dice
        print('Welcome to Game of Greed')
        banker = Banker()
        round = 1
        loop = True
        print("(y)es to play or (n)o to decline")
        user_input=input("> ")
        if user_input == 'n':
            print('OK. Maybe another time')

        elif user_input == 'y':
            while loop and banker.balance <= 10000:
                while loop:
                    remainning_dice = 6
                    roundScore=0
                    print(f'Starting round {round}')
                    
                    user_choose='r'
                    while user_choose=='r':
                        rollDice= " ".join(str(item)for item in(self.roller(remainning_dice)))
                        print(f'Rolling {remainning_dice} dice...')                   
                        print(f"*** {rollDice} ***")
                        junk=GameLogic.calculate_score(rollDice)
                        if junk ==0 or remainning_dice==0:
                            self.zlich(rollDice,banker,round)
                            break
                        else:    
                            print("Enter dice to keep, or (q)uit:")
                            dice_input = input('> ')
                            if dice_input == 'q':
                                self.quit(banker)
                                loop = False
                                break
                            else:
                                if not GameLogic.validate_keepers(tuple(rollDice),tuple(dice_input)): 
                                        print("Cheater!!! Or possibly made a typo...")
                                        print(f"*** {rollDice} ***")
                                        print("Enter dice to keep, or (q)uit:")
                                        dice_input = input('> ')
                               
                                remainning_dice = remainning_dice - len(dice_input)
                                roundScore += GameLogic.calculate_score(dice_input)
                                banker.shelf(roundScore)
                                print(f'You have {banker.shelved} unbanked points and {remainning_dice} dice remaining')
                                print("(r)oll again, (b)ank your points or (q)uit:")
                                user_choose = input("> ")
                                if user_choose=="b":
                                    self.banker_bank(banker,roundScore,round)
                                    break
                                elif user_choose == "q":
                                    self.quit(banker)

                                elif user_choose=='r' and len(dice_input) ==6 and len(dice_input)==len(GameLogic.get_scorers(self.roller(remainning_dice))):
                                    
                                    remainning_dice = 6
                                    

                                    continue   
                    round+=1

                        
                             
    def zlich (rollDice,banker,round):
        print("****************************************\n**        Zilch!!! Round over         **\n****************************************")
        banker.clear_shelf()
        print(f"You banked 0 points in round {round}\nTotal score is {banker.balance} points")
        round=round+1 


    def banker_bank(banker,score,round):                   
        banker.bank()
        print(f"You banked {score} points in round {round}\nTotal score is {banker.balance} points")
        round=round+1
        banker.clear_shelf()

    def quit ( banker):
         print(f'Thanks for playing. You earned {banker.balance} points')
         
    def is_hot_dice(rollDice:tuple)->bool:
          rolls_has_value=GameLogic.get_scorers(rollDice)
          if sorted(rollDice)==sorted(rolls_has_value):
              return True
          return False

if __name__ == "__main__":
    playGmae = Game
    playGmae.play()       

