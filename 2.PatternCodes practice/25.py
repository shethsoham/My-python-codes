'''
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
  * * * * 
    * * * 
      * * 
        * 

'''
rows = 5
for i in range(0,rows):
    for j in range(0,rows-1-i):
        print(" ",end="")
    for j in range(0,i+1):
        print("*",end="")
    print()
for i in range(0,rows-1):
    for j in range(0,i+1):
        print(" ",end="")
    for j in range(0,rows-1-i):
        print("*",end="")
    print()