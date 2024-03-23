"""
Author: [sahil kumar singh]
Assignment / Part: HW7 - Q5 (depending on the file name)
Date due: 2022-11-11, 12:00pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

def get_matryoshka_list(original_list):
    matryoshka_list=[]
    list_1=[]
   
    
    
    for i in range(len(original_list)-1):
        if (original_list[i] < original_list[i+1]):
            list_1.append(original_list[i])
            if i==len(original_list)-2:
                list_1.append(original_list[len(original_list)-1])
                matryoshka_list.append(list_1)
                     
        else:
            list_1.append(original_list[i])
            matryoshka_list.append(list_1)
            list_1=[]
            if i == len(original_list)-2:
                list_1.append(original_list[len(original_list)-1])
                matryoshka_list.append(list_1)
    return matryoshka_list
           
def main():
    original_list = [1, 2, 3, 5, 20, 19, 3, 4, 7, 45, 100, 1, 1, 3]
    matryoshka_list = get_matryoshka_list(original_list)
    
    print(matryoshka_list)
main()
