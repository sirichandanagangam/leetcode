class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        for i in range(0,n+1):
            for j in range(0,n):
                if i not in nums:
                    return i
        
