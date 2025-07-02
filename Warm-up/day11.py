arr = [2,3,4,3,2,34,2,34,2]
brr=[]
for x in range(len(arr)):
    brr.append(arr[x]**2)
    
print(sorted(brr))


# [4, 4, 4, 4, 9, 9, 16, 1156, 1156]


# 7. Reverse Integer
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



class Solution:
    def reverse(self, x: int) -> int:
        if x ==0:
            return 0
        xcopy = x
        x = abs(x)
        res = 0
        while x>0:
            lastid = x%10
            res = (10*res)+lastid
            x=x//10

        if res < (-2**31) or res > (2**31):
            return 0 
        return -res if (xcopy < 0) else res
