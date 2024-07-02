"""Himanshi has a text file and she wants to check whether that file contains any numerical value. 
So to help Himanshi write a python program that can check whether the text file includes any numerical value or not. 
As text files contain so many lines, so print the line number that has numerical values"""

f2 = open("number.txt","r")
line_count = 0
for x in f2:
    line_count += 1
    if any(i.isdigit() for i in x):
        print("The line",line_count,"has numerical value:",x.strip())
