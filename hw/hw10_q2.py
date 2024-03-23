"""
Author: [sahil kumar singh]
Assignment / Part: HW10 - Q2 Artist of the year
Date due: 2022-12-08, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

from hw10_q1 import Instrument
import random
class Musician:
    def __init__(self,stage_name,instrument=[]):
        self.stage_name=stage_name
        self.instrument=instrument
        self.number_of_instruments=len(instrument)
        
       
    def __str__(self):
        output=''
        for i in range(1,len(self.instrument)):
            if len(self.instrument)==1:
                output=str(self.instrument[0])
            elif i==len(self.instrument)-1:
                output+=',and a '+str(self.instrument[i])
            else:
                output+=', '+str(self.instrument[i])
        return 'Musician object '+"'"+self.stage_name+"',"+'owning a '+str(self.instrument[0])+output
    def pick_instrument(self,index=None):
        if index==None:
            
            return random.choice(self.instrument) 
        elif index>len(self.instrument)-1:
            return self.instrument[-1]
        elif len(self.instrument)==0:
            return None
        else:
            return self.instrument[index]


