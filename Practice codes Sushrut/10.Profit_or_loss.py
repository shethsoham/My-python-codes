#

cost_price = int(input("Enter the cost price"))
selling_price = int(input("ENter the selling price"))

loss = cost_price - selling_price
profit = selling_price - cost_price

if cost_price > selling_price :
    print (f"It's a lost of {loss} $")
elif cost_price == selling_price :
    print("Cost price and loss are same")
else : 
    print(f"It's a ptofit of {profit}$")