# program to check if a given number is Armstrong number or not.

user_input = int(input("Enter your number"))
str_length = str(user_input)
length = len(str_length)
print(length)

num = user_input 
a = num % 10
num = num  // 10

b = num % 10
c = num //10

if (a**3)+(b**3)+(c**3)== user_input:
    print("Armstrong Number")
else: 
    print("Not a armstrong number ")

