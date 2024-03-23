"""
Author: [sahil kumar singh]
Assignment / Part: HW4 - Q4 (Mod culture)
Date due: 2022-10-14, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
        
value=int(input("Enter value for n: "))
for i in range(1,value+1):
    even=0
    odd=0
    k=i
    while(k>0):
        if k%2==1:
            odd+=1
        else:
            even+=1
        k=k//10
    if even>odd:
        print(i,end=' ')
        
