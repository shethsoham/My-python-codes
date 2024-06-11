#If the input is leap year or not 


year_you = int(input("Enter the year you want to check"))

if year_you % 4 == 0 and (year_you % 100 != 0 or year_you % 400 == 0 )  :
    print("It is a leap year")
else :
    print("It's not a leap year")