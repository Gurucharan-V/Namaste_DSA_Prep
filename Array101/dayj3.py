# 26. Remove Duplicates from Sorted Array
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. 
# The remaining elements of nums are not important as well as the size of nums.a = [-9,-9,0,1,2,2,4,4,4,4,4,4,4,4,44,4,4,]
def remdups(arr):
    x=0
    for i in range(len(arr)):
        if arr[i] != arr[x]:
            x+=1
            arr[x] = arr[i]

    return (x+1, arr)
    
print(remdups(a))
