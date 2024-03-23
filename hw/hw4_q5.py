"""
Author: [Sahil Kumar Singh]
Assignment / Part: HW4 - Q5 ( Must be funny in the rich man  's world )
Date due: 2022-10-14, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
players=int(input("Enter a valid number of players: "))
while players < 2 or players>8:
    players=int(input("Enter a valid number of players: "))


value=0
for loop in range(players):
    assest=""
    sum=0

    while assest!="DONE":
        assest=input("Enter the value of a property assest, or DONE to finish: ")
        if assest!="DONE":
            sum +=float(assest)
            total=round(sum,2)
    print("player",loop+1,"has",total,"dollars.")    

    if sum>value:
        value=sum
        win=loop+1
print(win,"wins with",value,"dollars!")

