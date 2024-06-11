# How to Sum of the First N Positive Integers in Python
number = int(input("Emter the number you want to total"))
sum = 0 
for j in range(1,number+1):
    sum = sum + j

print(sum)

n = int(input("Enter the number till the point you want sum"))
summation = (n*(n+1))/2
print(summation)