#Calculate Inhabd salary 

# Tax  = 10 , 20 ,30 
# hra = 10 
# da = 5
# pf = 3 

user_salary = int(input("Enter the salary of the user "))

if user_salary >= 5000 and user_salary <= 10000 :
    tax = 10/100*user_salary
    temp_salary = user_salary - tax
elif user_salary >10000  and user_salary <= 20000:
    tax = 20/100*user_salary 
    temp_salary = user_salary - tax 
else:
    tax = 30/100 * user_salary
    temp_salary = user_salary - tax

print("tempapry salary after tax cut is ", temp_salary)


inhand_salary = temp_salary - ((10/100*user_salary)+(5/100*user_salary)+(3/100*user_salary))

print("Actual Inhand Salary is ", inhand_salary)