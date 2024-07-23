#Write a program which is divisible by 3 and 6 . 

check_Number = int(input("Enter the number you want to check"))

if check_Number % 3 == 0 and check_Number % 6 == 0 :
    print ("The nimber is divisible by 3 and 6 both")
elif check_Number % 3 ==0 or check_Number %6 ==0:
    print("The number is either divisible by 3 or 6" )
else :
    print("The number is not divisible by 3 and 6")

