"""
Author: [Sahil kumar singh]
Assignment / Part: HW3 - Q3 (Oh,Oh,Telephone Line, Give Me Some Time)
Date due: 2022-10-06, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
day = input("Enter the day the call started at: ")
time = int(input("Enter the time the call started at (hhmm): "))
duration = int(input("Enter the duration of the call (in minutes): "))

cost_m=duration*0.1
bill = round(cost_m,2)
cost_q=duration*0.55
cost = round(cost_q,2)
cost_w=duration*0.35
costw = round(cost_w,2)

if day == "Fri":
     print("This call will cost $",bill)
elif day == "Sat":
     print("This call will cost $",bill)
elif day == "Sun":
     print("This call will cost $",bill)
elif day == "Mon" and 2400>=time:
    if 2100>=time>=500:
        print("This call will cost $",cost)
    else:
        print("This call will cost $",costw)
elif day == "Tue" and 2400>=time:
    if 2100>=time>=500:
        print("This call will cost $",cost)
    else:
        print("This call will cost $",costw)
elif day == "Wed" and 2400>=time:
    if 2100>=time>=500:
        print("This call will cost $",cost)
    else:
        print("This call will cost $",costw)
elif day == "Thr" and 2400>=time:
    if 2100>=time>=500:
        print("This call will cost $",cost)
    else:
        print("This call will cost $",costw)
