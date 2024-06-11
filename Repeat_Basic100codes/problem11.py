# To calculate Profit or Loss for given selling and cost price.

cost_price = float(input("enter the cost price"))
selling_price = float(input("enter the selling price"))

profit = selling_price - cost_price 
loss = cost_price - selling_price

if profit > loss :
    print("It's a profit of", profit)
elif loss > profit :
    print("It's a loss of ", loss)
else : 
    print("There is no profit no loss")