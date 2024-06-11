# Python program to find the Factorial of a given number.

n = int(input("Enter the number whose factorial you want "))
# factorial of the number is 5! = 5*4*3*2*1 = 120
fact = 1
for i in range(1,n+1):
    fact = fact * i
    
       
print(fact)