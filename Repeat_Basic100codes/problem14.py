#  program to check if a given number is divisible by both 3 & 6.

input_number = int(input("Enter the number"))

if input_number % 3 == 0 and input_number % 6 ==0 :
    print("The number is divisible by both 3 and 6")
else:
    print("The number is not dividible by both ")