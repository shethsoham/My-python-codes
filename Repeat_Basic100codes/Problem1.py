# Python program to find the largest among 3 numbers entered by the user.

num1 = input("Enter the first number ")
num2 = input("Enter the second number")
num3 = input("Enter the third number ")

if num1 == num2 == num3 : 
        print("All 3  number are equal ") 

elif num1 >= num2 and num1 >=num3 : 
        if num1 == num2 > num3 : 
                print("Num1 and num2 are equal and greater than num3 ")
        elif num1 == num3 > num2 :
                print("Num1 and num3 are equal and greater than num2 ")
        else :
                print("num1 is greater than num2 and num3 ")

elif num2 >= num1 and num2 >=num3 : 
        if num1 == num2 > num3 : 
                print("Num1 and num2 are equal and greater than num3 ")
        elif num2 == num3 > num1 :
                print("Num2 and num3 are equal and greater than num1 ")
        else :
                print("num2 is greater than num1 and num3 ")
            
elif num3 >= num1 and num3 >=num2 : 
        if num3 == num1 > num2 : 
                print("Num1 and num3 are equal and greater than num2 ")
        elif num3 == num2 > num1 :
                print("Num3 and num2 are equal and greater than num1 ")
        else :
                print("num3 is greater than num1 and num2 ")

else:
        print("Try again ")