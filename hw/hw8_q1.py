"""
Author: [Sahil kumar singh]
Assignment / Part: HW8 - Q1 ((Probably) The Most Famous Computer Science Problem Eve)
Date due: 2022-11-17, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

from pprint import pprint

def get_nucleotide_frequencies(sequence):
    
    sequence=sequence.upper()
    Dic ={'A':0, 'C':0, 'G':0, 'Junk':{}, 'T':0}

    for i in sequence:
        if i=='A' or i=='C' or i=='G' or i=='T':
            Dic[i]= Dic[i]+1    
        elif i not in Dic['Junk']:
            Dic['Junk'][i]=1   
        else:
            Dic['Junk'][i]+=1
    junk_count = 0
    for key in Dic['Junk']:
        junk_count += Dic['Junk'][key] #gets the value
    return (Dic, junk_count)

def main():
    frequencies, junk_count=get_nucleotide_frequencies("ACTGTCaCGRFRTNfsHYCgggTCGACCSGTGTCACGT")
    pprint(frequencies)
    print(f"Number of junk nucleotides:",junk_count)
main()

