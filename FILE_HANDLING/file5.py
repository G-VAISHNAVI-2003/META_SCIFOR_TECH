"""Arunima created a text file on programming where she wrote the word language incorrectly many times. 
Now she wants to replace the incorrect word with the correct word. 
Doing it manually can take a lot of time plus she can miss out few words at the end. 
To help Arunima to replace the words write a python program. 
Use the concept of file handling and make changes in the text file. """

f5 = open("replace.txt","r")
data = f5.readlines()

f5 = open("replace.txt","w")
for i in data:
    x = i.replace("langauge","language")
    f5.write(x)
