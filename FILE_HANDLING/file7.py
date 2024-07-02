"""Nidhi has a bad habit of repeating the same word while typing. 
She wants a program that can remove duplicate phrases from paragraphs written by her. 
To help Nidhi write a python program that can connect with a text file and remove repeating words. 
"""
f7 = open("repeat.txt","r")
data = f7.readlines()
phrase = set()
new_list = []
for i in data:
    if i not in phrase:
        new_list.append(i)
        phrase.add(i)
f7 = open("repeat.txt","w")
f7.writelines(new_list)

