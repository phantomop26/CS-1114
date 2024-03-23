"""
Author: [Sahil Kumar Singh]
Assignment / Part: HW5 - Q1 (Working With Limitations)
Date due: 2022-10-20, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
upper_case="A,B,C,D,E,F,G,H,I,J,K,L,M,NO,P,Q,R,S,T,U,V,W,X,Y,Z"
lower_case="a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
upper=0
lower=0

text=str(input("Say something: "))
for j in text:
    if j in "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z":
        upper+=1
    elif j in "A,B,C,D,E,F,G,H,I,J,K,L,M,NO,P,Q,R,S,T,U,V,W,X,Y,Z":
        lower+=1
                                      
for i in range(len(text)):
    if text[i]>='A' and text[i]<='Z':
        st=text[i]
        st=ord(st)
        st=st+32
        st=chr(st)
        text=text[:i]+st+text[i+1:]
print(text)

print("Number of changed letters: ", lower)
print("Number of unchanged letters: ", upper)
print("Number of non-alphabetic characters: ", len(text)-(lower+upper))
        
