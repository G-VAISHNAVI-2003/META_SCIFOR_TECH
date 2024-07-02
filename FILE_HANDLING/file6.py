"""Ayman wants to modify one of his text files.
 In his text file, he wants to start a new line whenever he encounters a number followed by a period(.). 
So he decides to do the same with the help of the python program. Write a program for Ayman"""

f6 = open("newline.txt", "r") 
data = f6.read()

modified_data = ""

for i, c in enumerate(data):
    if  data[i] == ".":
        modified_data += c + '\n'
    else:
        modified_data += c

f6 = open("newline.txt", "w")
f6.write(modified_data)
