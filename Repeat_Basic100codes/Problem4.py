# Python code to add the digits of the number entered by the user

number = int(input("Enter the 3 digit number you want"))

x = number % 10 # 625 % 10 = 5

number = number // 10 # 625 // 10 = 62
y = number % 10 # 62 % 10 = 2
z = number // 10 # 62 //10 = 6

print(x+y+z)



