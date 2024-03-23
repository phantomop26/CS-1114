"""
Author: [Sahil Kumar Singh]
Assignment / Part: HW5 - Q2 (Complementary Service)
Date due: 2022-10-20, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
pair_1=0
pair_2=0
seq=""
comp=""
invalid_char=0

dna=input("Enter a DNA sequence: ")
sec_dna=input("Enter a second DNA sequence: ")

for pair_2 in range(len(sec_dna)):
    fused=""
    fused = dna[pair_1]+sec_dna[pair_2]
    pair_1+=1
    seq += fused
    
while pair_1 < len(dna):
    fused=dna[pair_1]
    pair_1+=1
    seq+=fused
    
for pair in range(len(seq)):
    if seq[pair]=="A":
        comp+="T"
    elif seq[pair]=="G":
        comp+="C"
    elif seq[pair]=="C":
        comp+="G"
    elif seq[pair]=="T":
        comp+="A"
    else:
        invalid_char+=1

print("Fused sequence: ",comp, "| Invalid characters: ",invalid_char)