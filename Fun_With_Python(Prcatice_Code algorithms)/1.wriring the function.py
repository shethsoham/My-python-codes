#Swapping of two elements usinfg function declaration 

a = int(input("Enter the value of a"))#value of a
b = int(input("Enter the value of b"))#value of b

def swap(a,b): # swap function without return
    temp=a
    a=b
    b=temp
    return a,b 

a, b = swap(a,b)

print("After swap value of a is ",a)
print("After swap the value of b is ",b)

#The program runs in order of O(1)