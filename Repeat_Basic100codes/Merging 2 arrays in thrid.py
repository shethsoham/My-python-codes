array1 = [1,2,3,4]
array2 = [1,2,2,3,3,5]

array3 = []

i = 0
j = 0

length = len(array1) + len(array2)
print(length)

for m in range(0,length-1):
        if array1[i]>=array2[j]:
            array3.append(array1[i])
            j = j+1

        else :
            array3.append(array1[j])
            i = i+1
            
print(array3)