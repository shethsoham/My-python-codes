#Menu Driven Program 

print("""
      Hello, what options would you like to select ?(Reply the exact number )
      1. Converting cm to inches 
      2. Converting kms to miles
      3. Converting usd to inr
""")


user_input = int(input("Enter the number"))

if user_input == 1 :
    cm = float(input("Enter the value in cm "))
    inches = cm * 0.394
    print("coversion from cm to inches is ", inches)
elif user_input == 2 : 
    kms = float (input("Enter the value in km "))
    miles = 0.621*kms
    print("conversion from km to miles ", miles)
elif user_input == 3 :
    usd = float(input("Enter the value in usd"))
    rs =  usd* 84.38
    print("Conversion from usd to inr is ", rs)
else :
    print("Wrong input")
