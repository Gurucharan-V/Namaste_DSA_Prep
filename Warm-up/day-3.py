# Write a Python function that takes a list of integers and returns the index of the largest number in the list. If the largest number appears multiple times, return the index of its first occurrence.

# Example input: [1, 2, 3, 4, 5, -2, 7]
# Expected output: 6 (since 7 is the largest and at index 6)

arr = [1,2,3,4,5,-2,7]
def idxlar(n):
    a = 0
    for x in range(len(n)):
        if n[x] > a:
            a = n[x]
    
    for y in range(len(n)):
        if n[y] == a:
            return y

print(idxlar(arr))


#Question
# Write a function that returns the smallest number in an array. 

# Input: arr = [2, -6, 4, 8, 1, -9]
# Output: -9


def smlnum(n):
    b=0
    for x in n:
        if x < b:
            b = x
    return b

print(smlnum(arr))


# Write a function that returns the largest number in an array.

# Approach
# Initialize a variable largest to -Infinity.
# Loop through the array.
# If the current element is greater than largest, update largest.
# Return largest after the loop ends.



def larger(n):
    b=0
    for x in range(len(n)):
        if n[x] > b:
            b = n[x]
    return b

print(larger(arr))
