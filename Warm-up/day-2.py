# Question:
# You are provided with a list of integers. Write a Python program to perform the following tasks:
# Determine and print the total number of elements in the list.
# Using a while loop, iterate through the list and separate the values into two new lists:
# One containing all odd numbers
# One containing all even numbers
# Sort both the odd and even lists in ascending order.
# Display the sorted lists along with appropriate labels ("odd" and "even").

# Constraints:
# Use a while loop for iteration.
# Do not use list comprehensions or built-in functions like filter().
# Note: Focus on clarity and correct categorization of numbers based on parity.


let = [1,2,3,3,34,3,42,43,24,234,32,4,23,43,24,2,423,4,234,24,2,34,2,424,3]

odd,even =[],[]


print(len(let),"\n")

i = 0
while i<len(let):
    if let[i] % 2 == 0:
        even.append(let[i])
    else:
        odd.append(let[i])
    i+=1   
    
odd.sort()
even.sort()
print(odd, "odd\n")
print(even, "even")


# Write a Python function named holy(n) that takes a number n as input and performs the following:
# Search through a predefined list let = [1, 2, 3, 3, 34, 3].
# Return the index of the first occurrence of n in the list.
# If the number n is not found, return -1.
# The function is then called with n = 12, and the result is printed.
# Note:
# You must use a for loop with indexing (i.e., range()).
# Do not use built-in functions like index().



m = [1, 2, 3, 3, 34, 3]
n=34
def findthidx(n,m):
    for x in range(len(m)):
        if m[x] == n :
            return x
    return -1
    
    
a = findthidx(4,m)
print(a)

#this is using the while loop
i=0
n=-1
found = False
while i < len(arr):
    if arr[i] == n:
        print(i)
        found = True
    i+=1
    
if not found:
    print("-1")

# Question
# Write a function that returns the number of negative numbers in an array.

# Approach
# Initialize a counter to 0.
# Loop through the array.
# If the element is less than 0, increment the counter.
# Return the final count after the loop ends.
# Example

# Input: 
arr = [2, -6, 4, 8, 1, -9]
# Output: 2
  
# Time & Space Complexity
# Time Complexity: O(n) – where n is the number of elements in the array.
# Space Complexity: O(1) – only a counter variable is used.

#using for
arr = [12,3,12,32,31,31,23,-45,3,42,-42,-34,-31,4,-14,-13,]



def findneg(n):
    a = 0
    for x in arr:
        if a > x:
            a = x
    print(a)
    
    
findneg(arr)


#using while

a=0
while n < len(arr):
    if arr[n] < a:
        a = arr[n]
    n+=1
    
print(a)





