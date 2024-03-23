"""
Author: [Sahil Kumar Singh]
Assignment / Part: HW10 - Q3 Battle of the bands
Date due: 2022-12-08, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
from hw10_q1 import Instrument
from hw10_q2 import Musician
import random
def get_name_of_battle_winner(object1,object2):
    
    list1=object1.instrument
    list2=object2.instrument
    random1=random.randint(0,len(list1)-1)
    random2=random.randint(0,len(list2)-1)
    
    if len(list1)==0 and len(list2)!=0:
        return 'NO CONTEST'
    elif len(list1)==0 and len(list2)!=0:
        return object2.stage_name
    elif len(list2)==0 and len(list1)!=0:
        return object1.stage_name
    else:
        instrument1=list1[random1]
        instrument2=list2[random2]
        print("{} picked a {}".format(object1.stage_name,instrument1))
        print("{} picked a {}".format(object2.stage_name,instrument2))
        

        if instrument1.strength>instrument2.strength:
            if instrument1.does_break()==True:
                print("{} 's {} broke".format(object2.stage_name,instrument2.model))
                return object1.stage_name
            else:
                print("{} 's {} broke".format(object1.stage_name,instrument1.model))
                return object2.stage_name
        elif instrument1.strength<instrument2.strength:
            if instrument2.does_break==True:
                return object1.stage_name
            else:
                return object2.stage_name
        elif instrument1.strength==instrument2.strength:
            print("Both musician's instruments are the same strength. The winner will be decide by the whim of chance.")
            chance_list=[object1.stage_name,object2.stage_name]
            chance=random.randint(0,1)
            print("{} 's {} broke".format(object2.stage_name,instrument2.model))
            return chance_list[chance]
        
    
def main():
    danelectro = Instrument("Stock '59", "Danelectro", 0.25)
    fender_vi = Instrument("VI Bass", "Fender", 0.99)
    four_double_o_one = Instrument("4001C64 Bass", "Rickenbacker", 0.856)
    gear = [danelectro, fender_vi, four_double_o_one]
 # Let's say both musicians have access to the same gear
    sad_musician = Musician("Robert Smith", gear)
    less_sad_musician = Musician("Miki Berenyi", gear)
 # Testing the get_name_of_battle_winner method a few times
    number_of_duels = 10
    for duel_number in range(number_of_duels):
        winner_name = get_name_of_battle_winner(sad_musician,less_sad_musician)
        print(f"THE WINNER OF DUEL #{duel_number + 1} IS {winner_name}!", end="\n\n")
main()
        
    
