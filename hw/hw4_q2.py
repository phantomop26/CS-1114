"""
Author: [sahil kumar singh]
Assignment / Part: HW4 - Q2 (Like An Hourglass)
Date due: 2022-10-14, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
num_of_rows=int(input("no of 2n lines: "))

#upper piece
for i in range(num_of_rows,0,-1):
    for j in range(num_of_rows-i):
        print(" ", end="")
    for j in range(1,2*i):
        print("*", end="")
    print()
#lower piece without the middle one
for i in range(2,num_of_rows+1):
    for j in range(num_of_rows-i):
        print(" ", end="")
    for j in range(1,2*i):
        print("*", end="")
    print()

    


