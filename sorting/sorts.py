ar = [3,2,1,4,0]


def bubsrt(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j+1] < arr[j]:
                arr[j+1],arr[j] =arr[j],arr[j+1]
                
    return arr
        
print(bubsrt(ar))


def selsrt(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[min] > arr[j]:
                min = j
            
            arr[min],arr[i] = arr[i],arr[min]
            
    return arr
    
print(selsrt(ar))


def isrtsrt(arr):
    for i in range(1,len(arr)):
        cur = arr[i]
        prev = i-1
        while(prev >=0 and arr[prev] > cur):
            arr[prev+1] = arr[prev]
            prev -=1 
            
        arr[prev+1] = cur
        
    return arr
        
print(isrtsrt(ar))
            
