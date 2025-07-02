arr = [2,3,4,3,2,34,2,34,2]
brr=[]
for x in range(len(arr)):
    brr.append(arr[x]**2)
    
print(sorted(brr))


# [4, 4, 4, 4, 9, 9, 16, 1156, 1156]
