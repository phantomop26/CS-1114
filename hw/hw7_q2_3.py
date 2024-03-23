"""
Author: [Sahil Kumar Singh]
Assignment / Part: HW7 - Q2 and Q3 (Of Code And Poetry)
Date due: 2022-11-11, 12:00pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
def is_haiku(input_string):
    lines=input_string.split("/")
    if len(lines)==3:
        line1=lines[0].split(",")
        line2=lines[1].split(",")
        line3=lines[2].split(",")
        if len(line1)==5 and len(line2)==7 and len(line3)==5:
            return True
        elif len(line1)!=5 and len(line2)==7 and len(line3)==5:
            print("WARNING: The first line is not 5 syllables long.")
            return False
        elif len(line1)==5 and len(line2)!=7 and len(line3)==5:
            print("WARNING: The second line is not 7 syllables long.")
            return False
        elif len(line1)==5 and len(line2)==7 and len(line3)!=5:
            print("WARNING: The third line is not 5 syllables long.")
            return False
print(is_haiku("clouds ,mur,mur ,dark, ly/it ,is ,a ,blin,ding,ha,bit/ga,zing ,at ,the ,moon"))
print("\n")

print(is_haiku("clouds ,mur,mur ,dark,ly/it ,is ,a ,blin,ding ,ha,bit/ga,zing"))
print("\n")



def haiku_string_parser(input_string):
    if "/" in input_string:
        comma_remove=input_string.replace(",","")
        slash_replace=comma_remove.replace("/","\n")
        return "".join(slash_replace)
    else:
        return ""


def main():
    haiku_string = "clouds ,mur,mur ,dark,ly/it ,is ,a ,blin,ding, ha,bit/ga,zing ,at ,the ,moon"
    formatted_haiku = haiku_string_parser(haiku_string)
    print(formatted_haiku)
main()
