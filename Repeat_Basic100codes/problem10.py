# Python program to check if the given 3 angles can form a triangle or not. 

a1 = float(input("enter the first angle"))
a2 = float(input("Enter the second angle"))
a3 = float(input("enter the third angle"))

sum = a1+a2+a3

if sum == 180:
    print("It is a traingle as the addition of the angle is",sum)
else:
    print("It is not a triangle as the addition of the angle is ", sum)