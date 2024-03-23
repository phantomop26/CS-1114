"""
Author: [Sahil Kumar Singh]
Assignment / Part: HW2 - Q4 (Collective Timetables)
Date due: 2022-09-29, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
##INPUT

day=int(input("Please enter the number of days Semi has worked: ")) 
hour=int(input("Please enter the number of hours Semi has worked: ")) 
minute=int(input("Please enter the number of minutes Semi has worked: "))

days=int(input("Please enter the number of days Daniel has worked: ")) 
hours=int(input("Please enter the number of hours Daniel has worked: ")) 
minutes=int(input("Please enter the number of minutes Daniel has worked: "))


##OPERATIONS
total_time= day*24*60 + hour*60 + minute + days*24*60 + hours*60 + minutes
din = (total_time//60)//24
ghante = total_time%(24*60)//60
min = total_time-(din*24*60 + ghante*60)




##OUTPUT
print("The total time both of them worked together is:", din,"days, ", ghante,"hours and ", min, "minutes") 
