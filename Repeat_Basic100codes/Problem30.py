#Python program to check a number is Prime or not.

num = int(input("Enter the number you want to check is prime or not "))

if num == 2 :
    print("it's a prime number ")
elif num>2 :
    for i in range(2, num ):
            if num % i == 0 :
                print("It is not a prime number ")
                break 
            else :
                print("It is a prime number ")
                break