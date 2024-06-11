#Python program to find the euclidean distance .
'''
The formula for Euclidean distance in two dimensions is D = ( x 2 − x 1 ) 2 + ( y 2 − y 1 ) 2 , 
where D is the Euclidean distance, and ( x 1 , y 1 ) and ( x 2 , y 2 ) are the Cartesian coordinates of the two points.
'''

x1 = float(input("Enter the x1 cordinate "))
x2 = float(input("Enter the x2 cordinate "))
y1 = float(input("Enter the y1 cordinate "))
y2 = float(input("Enter the y2 cordinate "))


euclidean_distance = ((x2-x1)**2 + (y2-y1)**2)**0.5

print("Euclidean distance is ", euclidean_distance)