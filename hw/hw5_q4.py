"""
Author: [Sahil Kumar Singh]
Assignment / Part: HW5 - Q4 (So it goes when you do your scales and your arpeggios)
Date due: 2022-10-20, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
import arpeggiator

ARPEGGIATOR = arpeggiator.Arpeggiator()
UP = arpeggiator.Direction.UP
DOWN = arpeggiator.Direction.DOWN



notes=input("Enter a musical note (i.e. A, Db, C#, etc.) or 'DONE' to end: ")

while notes!="DONE":
    ARPEGGIATOR.add_note(notes)
    if notes== "Ab, A#, A, Bb, B, C#, C, Db, D#, D, Eb, E, F#, F, Gb, G#, G,DONE":
         print("Note",notes,"added")
   
    else: 
         notes=input("Enter a musical note (i.e. A, Db, C#, etc.) or 'DONE' to end: ")
         print("WARNING:",'notes' ,"is not a valid note.","VALID NOTES: Ab, A#, A, Bb, B, C#, C, Db, D#, D, Eb, E, F#, F, Gb, G#, G\n")    

print(ARPEGGIATOR)        


up_down=input("Enter an arpeggiator direction [U/D]")
while up_down not in "U,D":
    up_down=input("Enter an arpeggiator direction [U/D]")
    



reps=int(input("How many times do you want your arpeggiator to play? "))

if up_down=="D" or up_down=="U":
    while reps<0:
        reps=int(input("How many times do you want your arpeggiator to play? (Must be positive amount)"))

    if reps>0:
        for i in range(0,reps+1):
            if up_down=="U":
                ARPEGGIATOR.play(UP)
            elif up_down=="D":
                ARPEGGIATOR.play(DOWN)

               
                
               
                
                
