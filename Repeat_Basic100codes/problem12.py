# simple intrest = P * R * T / 100

Principle_amount = float(input("The amount you want to borrow"))
Rate_of_intrest = float(input("The rate of intrest is "))
Time_period = float(input("The time period to return the amount taken"))

simple_intrest = Principle_amount * Rate_of_intrest * Time_period / 100
 
print("The simple intrest is ", simple_intrest)

total_amount = simple_intrest + Principle_amount

print("The total amount is ",total_amount)