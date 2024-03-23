"""
Author: [Sahil Kumar Singh]
Assignment / Part: HW2 - Q1 (Gravity Don't Pull Me)
Date due: 2022-09-29, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
##INPUT
mass_first=input("Enter the mass of the first object:")
mass_first=float(mass_first)

radius_first=input("Enter the radius of the first object:")
radius_first=float(radius_first)

mass_second=input("Enter the mass of the second object:")
mass_second=float(mass_second)

radius_second=input("Enter the radius of the second object:")
radius_second=float(radius_second)

distance=input("Enter the distance between the surfaces of both objects:")
distance=float(distance)

##CALCULATIONS
G = 6 * 10 ** -11
total_distance=distance + radius_second + radius_first
force = (G*mass_first*mass_second)/total_distance**2

##OUTPUT
print("The force of gravitation between these two objects is",force, "N.")


 


