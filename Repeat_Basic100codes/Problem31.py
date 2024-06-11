# Python program to print Armstrong number in the range 100 to 1000

num = int (input ("Enter the number you want to check "))

# 153 = 1**3 + 5 **3 + 3**3 

first  = num % 10 
num = num//10
second = num % 10
num = num // 10

print(first**3 + second**3 + num **3 )
