"""Create a text file aboutPython.txt ● Copy the given content in that file ● Using python read the content of the file. ● Use the concept of file handling."""
f1 = open("aboutPython.txt","r")
content = f1.read()
print(content)