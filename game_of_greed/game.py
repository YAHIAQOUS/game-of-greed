from game_logic import GameLogic

class Game:
    def __init__(self):
        self.roller=GameLogic.roll_dice

    def play():
        print('Welcome to Game of Greed')
        round = 1
        userInput=input("(y)es to play or (n)o to decline \n > ")
        if userInput == 'n':
            print('OK. Maybe another time')

        elif userInput == 'y':
            print(f'Starting round {round} \n Rolling 6 dice...')
            rollDice= " ".join(str(item)for item in(GameLogic.roll_dice()))
            print(f"*** {rollDice} ***")
            print("Enter dice to keep, or (q)uit:")
if __name__ == "__main__":
        
    playGmae = Game
    playGmae.play()       

