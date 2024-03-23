"""
Author: [Sahil Kumar Singh]
Assignment / Part: HW3 - Q1 (Are You Experienced?)
Date due: 2022-10-06, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

xp = float(input("Enter this user's current XP: "))
if xp>50.0:
    print("ERROR: Please enter a valid XP value.")
elif 50.0>=xp>=40.0:
    print("Level 5 Player (XP:",xp,")")
elif 39.9>=xp>=30.0:
    print("Level 4 Player (XP:",xp,")")
elif 29.9>=xp>=25.0:
    print("Level 3 Player (XP:",xp,")")
elif 24.9>=xp>=18.0:
    print("Level 2 Player (XP:",xp,")")   
else:
    print("Level 1 Player (XP:",xp,")")

    
