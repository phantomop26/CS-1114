"""
Author: [Sahil kumar singh]
Assignment / Part: HW3 - Q2 (It's Super Effective!)
Date due: 2022-10-06, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

import random
level=int(input("What is this Pokémon's level? "))
speed=int(input("What is this Pokémon's speed? "))



r=random.randint(0,255)
if 255>=(speed/2)>=0:
      if (speed/2) > r:
           m=(2*level+6)/(level+6)
           a=round(m,2)
           print("The Pokémon's move will be",a,"x stronger!")
      else:
          print("Pokemon didn't land a critical hit.")

    
