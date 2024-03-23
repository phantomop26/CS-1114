"""
Author: [Sahil Kumar Singh]
Assignment / Part: HW2 - Q3 (Oh No! The Pokémon Broke Free!)
Date due: 2022-09-29, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
import random
##INPUT
maximum = input("Entee the value of HPmax;")
maximum = int(maximum)

##OPERATIONS
current_health = random.randint(0,255)
ball = random.randint(0,255)
probablity = int(((maximum*255*4)/(current_health*ball)))
pseudo_number = random.randint(0,255)

##OUTPUT
print("Pokemon got caught:", (probablity>=pseudo_number))
