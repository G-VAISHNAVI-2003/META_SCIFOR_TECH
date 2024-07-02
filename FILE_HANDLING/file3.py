"""Shubham had created a BMI calculator to check his health condition daily. 
But he is not able to record the values. He wants to see how his BMI is changing. 
So he decided to connect his BMI program with a text file using the concept of file handling.
Now, when he uses his BMI program, his height, weight, BMI, and date get added to a text file "bmi.txt".
Create a program that can do the same thing for you."""

f3 = open("bmi.txt","a+")
n = input("Enter your name:")
a = int(input("Enter your weight in kg:"))
b = int(input("Enter your height in m:"))
bmi = a/(b**2)
#f3.write("The name is",n,"and his given weight and height are ",a,"and",b,"and his BMI:",bmi)
f3.write("The name is " + n + " and the given weight and height is " + str(a) + " kg and " + str(b) + " m and the BMI value is : " + str(bmi) + "\n")
f3.seek(0)
data = f3.read()
print(data)