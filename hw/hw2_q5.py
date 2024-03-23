"""
Author: [Sahil Kumar Singh]
Assignment / Part: HW2 - Q5 (Curb Your (Graduation) Privilege)
Date due: 2022-09-29, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

##INPUT
dean = input("Do you have permission from the dean? [y/n]")
advisor = input("Do you have permission from the advisor? [y/n]")
senior = input("Do you hold senior status? [y/n]")
credit = input("How many credits do you have?")
credit = int(credit)
##OPERATIONS
requirement = credit>=64 and senior == "y" or credit>=40 and advisor == "y" or dean == "y"



##OUTPUT
print("This student can graduate:", str(requirement))

