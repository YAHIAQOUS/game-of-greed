import abc
from random import randint
from typing import Counter

# from abc import ABC 
class GameLogic:

    @staticmethod
    def calculate_score(input)-> int:
        #"first diget num of repeatition second digt number it self " : value
        calculate_table={"25":100,"21":200,"11":100,"15":50,"31":1000,"41":2000,"51":3000,"61":4000,"32":200,"42":400,"52":600,"62":800,"33":300,"43":600,"53":900,"63":1200,"34":400,"44":800,"54":1200,"64":1600,"35":500,"45":1000,"55":1500,"65":2000,"36":600,"46":1200,"56":1800,"66":2400}
        choosen_map = {}
        score=0
             
        for item in input: 
            current_count = choosen_map.get(item, 0)
            choosen_map[item] = current_count + 1
        if len(choosen_map)==6:
                return 1500
        if  len(choosen_map)==3 and list(choosen_map.values())[0]==list(choosen_map.values())[1]==list(choosen_map.values())[2]:
            return 1500
        for item in choosen_map:
            target_element=f"{choosen_map[item]}{item}"
            if target_element in calculate_table:
                score+=calculate_table[target_element]
        
        return score

    @staticmethod 
    def roll_dice(num=6)->tuple:
        list_dice=[]
        for i in range(num):
            list_dice.append(randint(1,6))
        return tuple(list_dice)
        # return tuple((1,2,3,4,5,6))


    @staticmethod
    def get_scorers(input:tuple)-> tuple:
        #"first diget num of repeatition second digt number it self " : value
        calculate_table={"25":100,"21":200,"11":100,"15":50,"31":1000,"41":2000,"51":3000,"61":4000,"32":200,"42":400,"52":600,"62":800,"33":300,"43":600,"53":900,"63":1200,"34":400,"44":800,"54":1200,"64":1600,"35":500,"45":1000,"55":1500,"65":2000,"36":600,"46":1200,"56":1800,"66":2400}
        choosen_map = {}
        score=()
             
        for item in input: 
            current_count = choosen_map.get(item, 0)
            choosen_map[item] = current_count + 1
        if len(choosen_map)==6:
                return (1,2,3,4,5,6)
        if  len(choosen_map)==3 and list(choosen_map.values())[0]==2 and list(choosen_map.values())[1]==2 and list(choosen_map.values())[2]==2:
            for item in choosen_map:
                score+=(item,item)
            return tuple(sorted(score))
        for item in choosen_map:
            target_element=f"{choosen_map[item]}{item}"
            if target_element in calculate_table:
                Counter=0
                while int(target_element[0])>Counter:
                    Counter+=1  
                    score+=(int(target_element[1]),)
        
        return tuple(sorted(score))


    @staticmethod 
    def validate_keepers(roll, keepers):
        # Transform roll into list in order to use pop() method
        if type(roll) != tuple:
            roll = [roll]
        else:
            roll = list(roll)
        # Transform keepers into tuple if  it is not
        if type(keepers) != tuple:
            keepers = (keepers,)

        for i in keepers:
            if i in roll:
                roll.pop(roll.index(i))
            else:
                return False
        return True

if __name__=="__main__":
    game_logic=GameLogic()
    print (game_logic.validate_keepers((5, 2, 3, 5, 4, 2),(5)))

