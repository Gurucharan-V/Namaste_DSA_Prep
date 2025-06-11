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



