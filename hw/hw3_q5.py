"""
Author: [Sahil kumar singh]
Assignment / Part: HW3 - Q5 (What Is This, A Math Class?)
Date due: 2022-10-06, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

first=float(input("Length of the first side: "))
second=float(input("Length of the second side: "))
third=float(input("Length of the third side: "))

if first==second==third:
    print(first, second, third, "form an equilateral triangle")
elif first!=second!=third:
    print(first, second, third, "form a scalene triangle")
elif first==second or second==third or first==third:
    if first**2 + second**2 == third**2 or first**2 + third**2 == second**2 or second**2 + third**2 == first**2:
         print(first,",", second,",", third, "form an isosceles right triangle")    
    else:
         print(first, second, third, "form an isosceles triangle that is not a right triangle")
