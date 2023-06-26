X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
 
Z = []
for i in range(len(X)):
    for j in range(len(X[0])):
        
      Z[i][j] = X[i][j]+Y[i][j]

for r in Z:
   print(Z)

