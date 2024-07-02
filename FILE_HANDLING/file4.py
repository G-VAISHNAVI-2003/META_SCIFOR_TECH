"""Arvind has a huge text file and he wants to put a serial number at the beginning of each line. 
Doing this task manually can take a lot of time. He is not aware of python file handling. 
Write a python program that can put a serial number in front of each line in any specified text file"""

f4 = open("serial.txt","r")
data = f4.readlines()

f4 = open("serial.txt","w")
line_count = 1
for i in data:
    f4.write(str(line_count)+"."+ i)
    line_count += 1
