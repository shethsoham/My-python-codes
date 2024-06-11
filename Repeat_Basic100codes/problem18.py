#Narcissictic number
#4 Digit number #1634

user_input_1 = int(input("Enter the 4 digit number "))

number = user_input_1 #1634

a = number % 10 #4

number = number //10 # 163

b = number % 10  # 3
number = number // 10 # 16

c = number % 10 # 6

d = number // 10 # 1

calculation_number = (a**4 + b ** 4 + c ** 4 + d ** 4)
print(calculation_number)

if calculation_number == user_input_1:
    print ("It is a Narcissictic number")
else : 
    print ("It is not a Narcissictic number ")