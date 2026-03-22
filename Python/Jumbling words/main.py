import random
string_old=input("Enter a string: ")
string_old1=""

string_new=""

for i in range(len(string_old)):
    r=random.randrange(len(string_old))
    string_new=string_new+string_old[r]
    for j in range(0, len(string_old)):
        if j!=r:
            string_old1=string_old1+string_old[j]
    string_old=string_old1
    string_old1=""
print("The shuffled string is: ", string_new)