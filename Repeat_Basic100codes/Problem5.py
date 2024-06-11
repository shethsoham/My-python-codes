
# Reverse the input digit

number = 1234 
original_number = 1234

a = number% 10 # 4
number = number // 10 # 123 

b = number % 10 #3
number = number //10 # 10

c = number % 10 #2
d = number // 10 # 1

print("The original number is ", original_number )
print("The reverse number is ", a*1000 + b*100 + c*10 + d*1)
