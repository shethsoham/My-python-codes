#Leap year program | Python tutorial

# To be a leap year, the year number must be divisible by four – except for end-of-century years, which must be divisible by 400.
# This means that the year 2000 was a leap year, although 1900 was not. 2024, 2028, 2032 and 2036 are all leap years.

user_check_year = int(input("Enter the year you want to check "))

if (user_check_year % 4 == 0 or user_check_year % 100 != 0) and user_check_year % 400 == 0:
    print("This is a leap year")
else :
    print("This is not a leap year ")