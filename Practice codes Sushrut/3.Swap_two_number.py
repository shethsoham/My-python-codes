#Swwap two numbers

a = int(input("Enter the one number"))
b = int(input("Enter the second number"))

print("Previous Value of a is", a)
print("Previous Value of b is", b)
c = a
a = b
b = c

print("Value of a is", a)
print("Value of b is", b)