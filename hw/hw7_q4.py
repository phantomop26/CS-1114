"""
Author: [sahil kumar singh]
Assignment / Part: HW7 - Q4
Date due: 2022-11-11, 12:00pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

from dance_dance_revolution import DanceDanceRevolution
GAME = DanceDanceRevolution()


def get_game_parameters():
    
    
    amount=int(input("How many steps would you like to memorize? (positive non-zero integers only)"))
    while amount<=0:
        print("WARNING: Please enter a positive non-zero integer value.")
        amount=int(input("How many steps would you like to memorize? (positive non-zero integers only)"))
    speed=float(input("How fast would you like the game to run? (positive non-zero numerical values only)"))
    while speed<=0:
        print("WARNING: Please enter a positive non-zero integer value.")
        speed=float(input("How fast would you like the game to run? (positive non-zero numerical values only)"))
    tuple=()
    tuple+=amount, speed    
    return tuple

def get_user_answers():
    list=[]
    direction=input("Enter a direction (U/D/L/R) or 'DONE' to finish:")
    while direction =="DONE":
        print("Please enter at least one answer before selecting 'DONE'.")
        direction=input("Enter a direction (U/D/L/R) or 'DONE' to finish:")
    list.append(direction)
    while direction !="DONE":
        direction=input("Enter a direction (U/D/L/R) or 'DONE' to finish:")
        list.append(direction)
    return list

def run_game():
    amount_speed=get_game_parameters()
    amount, speed=amount_speed
    GAME.set_speed(speed)
    GAME.set_amount(amount)
    GAME.play_sequence()
    answers=get_user_answers()
    extra_done=answers.pop()
    boolean =GAME.check_answers(answers)
    if boolean== True:
        print("Congratulations! You've guessed correctly!")
    elif boolean == False:
        print("Wrong! Game Over!")
run_game()