#DocumentDistance LEC1

import math

def generate(filename):#function that generates the word-frequency vector
    list=[]
    frequency_list=[]
    word=""
    i=0
    frequency=1
    with open(filename) as File:
        
        for character in File.read():
            if character==" ":
                list.append(word.lower())
                word=""
            elif character=="." or character==",":
                list.append(word.lower())
                list.append(character)
                word=""
            else:
                word=word+character
    while "" in list:
        list.remove("")
    list.sort()
    word=""
    while i<len(list):
        word=list[i]
        if i+1!=len(list):
            if list[i]==list[i+1]:
                frequency=frequency+1
                
            else:
                frequency_list.append([f"{word}",frequency])
                frequency=1
        else:
            frequency_list.append([f"{word}",frequency])
                
        i=i+1
    return frequency_list


def distance_metric(V_1 , V_2):
    distance_metric=0
    for i in range(0,len(V_1)):
        for j in range(0,len(V_2)):
            if V_1[i][0]==V_2[j][0]:
                dot=V_1[i][1]*V_2[j][1]
                distance_metric=distance_metric+dot
    return distance_metric


def fraction(V_1,V_2):
    mod1,mod2=distance_metric(V_1,V_1)**0.5,distance_metric(V_2,V_2)**0.5


    div=mod1*mod2  
    res=distance_metric(V_1,V_2)/div
    return res    
                
                
                
"""-------------------------------------------------------------------------------------------EXPERIMENT BLOCK-------------------------------------------------------------------------------------------"""

D1=generate("file1.txt")
D2=generate("file2.txt")

print(f"The distance metric of the files is:{distance_metric(D1,D2)}")
print(f"The fraction of similiarity is:{fraction(D1,D2)}")

"""-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""