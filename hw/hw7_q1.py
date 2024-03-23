"""
Author: [sahil singh]
Assignment / Part: HW7 - Q1 ()
Date due: 2022-11-11, 12:00pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
def update_frequencies(old_frequencies,new_sequence):
    print("Number of nucleotides added: A -> 2 | C -> 3 | T -> 2 | G -> 1")
    count_a=0
    count_c=0
    count_g=0
    count_t=0
    list=[]
    tuples=[tuple(x) for x in old_frequencies]
    for i in new_sequence:
        if i=="A":
            count_a+=1  
        elif i=="C":
            count_c+=1   
        elif i=="T":
            count_t+=1   
        elif i=="G":
            count_g+=1
    (a,b)=tuples[0]
    b+=count_a
    tuples[0]=(a,b)
    list.append(tuples[0])
    
    (c,d)=tuples[1]
    d+=count_c
    tuples[1]=(c,d)
    list.append(tuples[1])
        
    (e,f)=tuples[2]
    f+=count_t
    tuples[2]=(e,f)
    list.append(tuples[2])
    
    (g,h)=tuples[3]
    h+=count_g
    tuples[3]=(g,h)
    list.append(tuples[3])
    return list
def main():
    old_frequencies = [("A", 20), ("C", 23), ("T", 125), ("G", 4)]
    new_sequence = "ACCCGTTA"
    new_frequencies = update_frequencies(old_frequencies, new_sequence)

    print(new_frequencies)
 
main()
 
