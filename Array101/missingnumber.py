# 268. Missing Number
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
# Example 1:

# Input: nums = [3,0,1]

# Output: 2


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        psum=0
        n=len(nums)
        tsum = int(n*(n+1)/2)
        for i in nums:
            psum+=i


        
        return tsum - psum

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxi=0
        for i in range(len(nums)+1):
            if i not in nums:
                maxi = i 

        return maxi

