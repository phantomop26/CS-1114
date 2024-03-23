"""
Author: Sahil Kumar Singh
Assignment / Part: HW6 - Q1 (Good vibrations)
Date due: 2022-10-20, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
from touchTypes import TouchType, SwipeDirection
SINGLE_TOUCH = TouchType.SINGLE_TOUCH
DOUBLE_TAP = TouchType.DOUBLE_TAP
SWIPE = TouchType.SWIPE
HOLD = TouchType.HOLD
UP = SwipeDirection.UP
DOWN = SwipeDirection.DOWN
LEFT = SwipeDirection.LEFT
RIGHT = SwipeDirection.RIGHT
NO_DIRECTION = SwipeDirection.NO_DIR



def get_touch():
    touch_type=input("What type of touch did the user perform? [single/double/swipe/hold]")
    
    register_touch(touch_type)
   
def register_touch(touch_type):
    if touch_type == "SINGLE" or touch_type == "single":
        touch=float(input("How strong was the user's touch? [0.0 to 1.0] "))
        print("Registering single touch...")
    elif touch_type == "DOUBLE" or touch_type =="double":
        touch=float(input("How strong was the user's touch? [0.0 to 1.0] "))
        print("Registering double tap...")
    elif touch_type == "SWIPE" or touch_type =="swipe":
        direction=input("In what direction did the user swipe?")
        touch=float(input("How strong was the user's touch? [0.0 to 1.0] "))
        print("Registering swipe...")
        if direction == "UP" or direction == "up":
            print("Exiting app...")
        elif direction =="LEFT" or direction =="left" or direction =="RIGHT" or direction == "right":
            print("Changing page...")
        elif direction =="DOWN" or direction == "down":
            print("Scrolling up...")
    elif touch_type=="HOLD" or touch_type =="hold":
        duration=float(input("For how long did the user hold the touch? "))
        strength=float(input("How strong was the user's touch? [0.0 to 1.0] "))
        print("Registering hold...")
        touch_ratio= strength/duration
        give_haptic_feedback(touch_ratio)
        
    
def give_haptic_feedback(touch_ratio):
    if 0<touch_ratio<0.5:
        print("Vibrating once...")
    elif 0.5<=touch_ratio<=2.0:
        print("Vibrating twice...")
    elif touch_ratio>2.0:
        print("Vibrating thrice...")

def main():
    get_touch()
    
main()
        
        


