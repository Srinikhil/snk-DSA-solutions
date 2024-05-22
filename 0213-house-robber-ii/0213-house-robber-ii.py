class Solution(object):
    def maxRob(self, nums):
        prev2, prev = 0, nums[0]
        
        for i in range(1, len(nums)):
            pick = nums[i]
            if i > 1:
                pick += prev2
            notPick = 0 + prev
            
            prev2 = prev
            prev = max(pick, notPick)
            
        return prev
            
    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self.maxRob(nums[:n-1]), self.maxRob(nums[1:]))
        
        
        