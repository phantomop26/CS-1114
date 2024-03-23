"""
Author: [sahil singh]
Assignment / Part: HW1 - Q4
Date due: 2022-09-22, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.\
"""


input("Please enter your amount of dollars and cents, in two separate lines.")
##INPUT
dollars = input()
dollars = int(dollars)
cents = input()
cents = int(cents)


##OPERATIONS

cent = dollars*100 + cents 
quarters = cent//25
dimes = (cent%25)//10
nickel = ((cent%25)//10)//5
pennies = cent%5



##OUTPUT
print(dollars,"dollars and", cents,"cents are:", quarters,"quarters,",dimes,"dimes,", nickel,"nickels and",pennies,"pennies.")
