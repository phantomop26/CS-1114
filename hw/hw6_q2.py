"""
Author: Sahil Kumar Singh
Assignment / Part: HW6 - Q2 (Le Grand Jour)
Date due: 2022-10-20, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
def get_decimal_time(hours, min, sec):
    sec_hours=60*60*hours
    sec_min=60*min
    sec=sec
    total_sec = sec_hours+sec_min+sec
    new_hour = total_sec//10000
    new_min = (total_sec%10000)//100
    new_sec = total_sec%100

    print(str(new_hour)+":"+str(new_min)+":"+str(new_sec))
    
def get_decimal_date(month,day,year):
    if day//10==1:
        decade=2
    elif day//10==2:
        decade=3
    else:
        decade=1
    french_year="Year "+str(year-1792)
    if month ==1:
        french_month= "Nivôse"
    elif month==2:
        french_month="Pluviôse"
    elif month==3:
        french_month="Ventôse"
    elif month==4:
        french_month="Germinal"
    elif month==5:
        french_month="Floréal"
    elif month==6:
        french_month="Prairial"
    elif month==7:
        french_month="Messidor"
    elif month==8:
        french_month="Thermidor"
    elif month==9:
        french_month="Fructidor"
    elif month==10:
        french_month="Vendémiaire"
    elif month==11:
        french_month="Brumaire"
    elif month==12:
        french_month="Frimaire"
    print(str(day)+" "+french_month+" "+french_year+", Décade "+str(decade))

    
     
def get_french_datetime(string):
    time,day=string.split(" ")
    hours,min,sec=time.split(":")
    month,day,year=day.split("/")
    get_decimal_time(int(hours),int(min),int(sec))
    get_decimal_date(int(month),int(day),int(year))
    
get_french_datetime("16:07:46 03/22/2022")

    
    
    
    
    
    
    
    
    
