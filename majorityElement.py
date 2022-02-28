class Solution(object):
    def majorityElement(self, nums):
        length, max,maxnumber = len(nums) , 0 , 0
        for i in range(0,length,1):
            count = nums.count(nums[i])
            l = length/2
            if(max < count):
               max = count
               if (max > l) : 
                    maxnumber = nums[i]
                    return maxnumber
               
                    
                    
   class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]
                    
                    
