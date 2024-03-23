"""
Author: [Sahil Kumar Singh]
Assignment / Part: HW5 - Q3 (Lexicographic Trends)
Date due: 2022-10-20, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
alpha=0
text=str(input("Please enter a string of lowercase letters: "))
for i in range(len(text)-1):
    if text[i]>text[i+1]:
        alpha+=1
if alpha==len(text)-1:
    print(text,"is decreasing")
else:
    print(text,"is not decreasing")


        
