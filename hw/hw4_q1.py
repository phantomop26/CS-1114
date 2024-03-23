"""
Author: [Sahil Kumar Singh]
Assignment / Part: HW4 - Q1 ((Odd) Baby Steps)
Date due: 2022-10-14, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""


positive=int(input("Please enter a positive integer: "))
print("Executing while-loop...")
i=1
while i<=positive*2:
    if i%2==1:
        print(i)
    i=i+1        

print("\nExecuting for-loop...")
for i in range(1, 2*positive+1,2):
    print(i)


