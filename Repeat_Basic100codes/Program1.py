# How to find average of N numbers in Python


user_input_number = int(input("enter the numberof digits you want to enter "))
print("Number of inputs enter buy the user ",user_input_number )
sum = 0
for i in range(0,user_input_number):

    take_number = int(input("enter the numbers you want to take as input "))
    sum = sum + take_number

print("Sum is",sum)

avg = sum / user_input_number 

print("Average is ",avg)