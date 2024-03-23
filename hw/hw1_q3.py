"""
Author: [sahil singh]
Assignment / Part: HW1 - Q3
Date due: 2022-09-22, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.\
"""
input("Please enter number of coins:")

##INPUT

quarters = input("Number of quarters:")
quarters = int(quarters)

dimes = input("Number of dimes:")
dimes = int(dimes)

nickels = input("Number of nickels:")
nickels = int(nickels)

pennies = input("Number of pennies:")
pennies = int(pennies)

##OPERATIONS
total = quarters*25 + dimes*10 + nickels*5 + pennies*1

##OUTPUT
print("The total is ", total//100, "dollar(s) and", total%100, "cent(s)")
