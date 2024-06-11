#Sum of first n number 

n = int(input("Enter the last number till which was the sum "))
sum = 0
for i in range(1,n):
    sum = sum + i 

print("Sum for n natural number is ", sum)