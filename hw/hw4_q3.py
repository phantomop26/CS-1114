"""
Author: [Sahil Kumar Singh]
Assignment / Part: HW4 - Q3 (Count Your Steps)
Date due: 2022-10-14, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

reps=int(input("Enter a positive integer: "))
steps=1
actual=0
number=1
while actual<reps:
    gap=reps-actual-1
    print((" "*gap)+str(number))
    increase=steps+1
    number=number+(increase*(10**(increase-1)))
    actual+=1
    steps+=1