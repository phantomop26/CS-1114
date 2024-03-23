"""
Author: [Sahil kumar singh]
Assignment / Part: HW3 - Q4 (Why, This Car Could Be Systematic, Programmatic, Quadratic!)
Date due: 2022-10-06, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
import math
a=float(input("Please enter value of a: "))
b=float(input("Please enter value of b: "))
c=float(input("Please enter value of c: "))

if a==0 and b==0 and c==0:
    print("This equation has infinite number of solutions.")
elif a==0 and 9>=b>=0 and 9>=c>=0:
    print("This equation has no solution.")
elif b==0 and 9>=a>=0 and 9>=c>=0:
    print("This equation has no real solutions.")
elif 9>=a>=0 and 9>=b>=0 and 9>=c>=0 and b**2==4*a*c:
    z=-b/2*a
    print("This equation has one real solution: x =",z)
elif 9>=a>0 and 9>=b>0 and 9>=c>=0:
    x1=(-b+(b**2-4*a*c)**1/2)/2*a
    x2=(-b-(b**2-4*a*c)**1/2)/2*a
    print("This equation has Two real soultions: x =",x1,"and",x2)
