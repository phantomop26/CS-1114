"""
Author: [sahil singh]
Assignment / Part: HW1 - Q2
Date due: 2022-09-22, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.\
"""
##INPUT
year = input("Please enter a year greater than 2022:\n")
year = int(year) 


##OPERATION
years = year - 2022
birth = (years*60*60*365*24)//9
death = (years*60*60*365*24)//18
immigrant = (years*60*60*365*24)//40
emigration = (years*60*60*365*24)//60

total = 330109174 + birth + immigrant - emigration - death 

##OUTPUT
print("The population in year", year,"will be",total)





























