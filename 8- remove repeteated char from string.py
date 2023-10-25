#8.Write a python program to Remove Repeated Character from String.

string = 'nnannnammhh'
string1=""
for i in string:
    if i not in string1:

        string1=string1+i
print(string1) 