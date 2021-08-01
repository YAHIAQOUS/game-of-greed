import abc
from random import randint

# from abc import ABC 
class GameLogic:

    @staticmethod
    def calculate_score(x:tuple)-> int:
        pass

    @staticmethod 
    def roll_dice(num=6)->tuple:
        list_dice=[]
        for i in range(num):
            list_dice.append(randint(1,6))
        return tuple(list_dice)

        

