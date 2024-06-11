#take 3 input for user and see if it triangle or not


angle1 = int(input("Enter the first angle "))
angle2 = int(input("Enter the second angle"))
angle3 = int(input("Enter the thord angle"))


if angle1 + angle2 + angle3 == 180 :
    print("It is a triangle")
else :
    print("It is not a triangle")