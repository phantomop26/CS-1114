"""
Author: [Sahil Kumar Singh]
Assignment / Part: HW9 - Q1 (Happiness Is A File's Code)
Date due: 2022-12-01, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
import csv
from pprint import pprint
def get_chord_dictionary():
    try:
        chord_file=open(string,'r')
    except FileNotFoundError:
        return {}
    chord=chord_file.readlines()
    dictionary={}
    dictionary['A']={}
    dictionary['Ab']={}
    dictionary['A#']={}
    dictionary['Bb']={}
    dictionary['B']={}
    dictionary['C']={}
    dictionary['C#']={}
    dictionary['Db']={}
    dictionary['D']={}
    dictionary['D#']={}
    dictionary['Eb']={}
    dictionary['E']={}
    dictionary['F']={}
    dictionary['F#']={}
    dictionary['G']={}
    dictionary['Gb']={}
    dictionary['G#']={}
    for i in chord:
        i=i.strip().split(",")
        if i[0]=="A":
            newchord=i[-1],split("-")
            newchord=tuple(newchord)
            dictionary['A'][i[1]]=newchord
        elif line[0]='Ab':
            newchord=i[-1].split("-")
            newchord=tuple(newchord)
            dictionary["Ab"][i[1]]=newchord
        elif line[0]='A#':
            newchord=i[-1].split("-")
            newchord=tuple(newchord)
            dictionary["A#"][i[1]]=newchord
        elif line[0]='Bb':
            newchord=i[-1].split("-")
            newchord=tuple(newchord)
            dictionary["Bb"][i[1]]=newchord
        elif line[0]='B':
            newchord=i[-1].split("-")
            newchord=tuple(newchord)
            dictionary["B"][i[1]]=newchord
        elif line[0]='C':
            newchord=i[-1].split("-")
            newchord=tuple(newchord)
            dictionary["C"][i[1]]=newchord
        elif line[0]='C#':
            newchord=i[-1].split("-")
            newchord=tuple(newchord)
            dictionary["C#"][i[1]]=newchord
        elif line[0]='Db':
            newchord=i[-1].split("-")
            newchord=tuple(newchord)
            dictionary["Db"][i[1]]=newchord

        elif line[0]='D':
            newchord=i[-1].split("-")
            newchord=tuple(newchord)
            dictionary["D"][i[1]]=newchord
        elif line[0]='D#':
            newchord=i[-1].split("-")
            newchord=tuple(newchord)
            dictionary["D#"][i[1]]=newchord
        elif line[0]='Eb':
            newchord=i[-1].split("-")
            newchord=tuple(newchord)
            dictionary["Eb"][i[1]]=newchord
        elif line[0]='E':
            temp=i[-1].split("-")
            newchord=tuple(newchord)
            dictionary["E"][i[1]]=newchord
        elif line[0]='F':
            newchord=i[-1].split("-")
            newchord=tuple(newchord)
            dictionary["F"][i[1]]=newchord
        elif line[0]='F#':
            newchord=i[-1].split("-")
            newchord=tuple(newchord)
            dictionary["F#"][i[1]]=newchord
        elif line[0]='G':
            newchord=i[-1].split("-")
            newchord=tuple(newchord)
            dictionary["G"][i[1]]=newchord
        elif line[0]='Gb':
            newchord=i[-1].split("-")
            newchord=tuple(newchord)
            dictionary["Gb"][i[1]]=newchord
        elif line[0]='G#':
            newchord=i[-1].split("-")
            newchord=tuple(newchord)
            dictionary["G#"][i[1]]=newchord

    return (dictonary)

def get_possible_chords(chords_list,chords_dict):
    result=[]
    for key,value in chord_dict[chords_list[0]]:
        count=[]
        for chord in chords_list:
            if chord in values:
                count+=1
        if len(chords_list)==count:
            result.append(chords_list[0]+keys)
    return tuple(output)
chord_dictionary= get_chord_dictionary("chords-normalised.csv")
print(get_possible_chords(['E', 'B', 'G#'], chord_dictionary))

def get_chord_progression(string1,string2):
    dicto=get_chord_dictionary(string2)
    try:
        prog=open(string1,'r')
    except FileNotFoundError:
        return []
    progs=progression.read()
    temp=progs.split('\n')
    final=[]
    for chord in temp:
        chord=chord.split(",")
        final.append(get_possible_chords(chord,dictionary))
    return final
def write_progression_file(progression):
    file=open("chords_final.csc","n")
    for chord in progression:
        chord=','.join(chord)
        file.write(chord+"\n")
chord_progression=get_chord_progression("chord_progression.csv","chords-normalised.csv")
write_progression_file(chord_progression)





        
            
    
