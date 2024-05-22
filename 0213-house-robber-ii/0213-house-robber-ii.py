class Solution(object):
    # Space Optimized approach
#     def maxRob(self, nums):
#         prev2, prev = 0, nums[0]
        
#         for i in range(1, len(nums)):
#             pick = nums[i]
#             if i > 1:
#                 pick += prev2
#             notPick = 0 + prev
            
#             prev2 = prev
#             prev = max(pick, notPick)
            
#         return prev

    def maxRob(self, nums, idx, dp):
        if idx == 0:
            return nums[0]
        if idx < 0:
            return 0
        if dp[idx] != -1:
            return dp[idx]
        
        pick = nums[idx] + self.maxRob(nums, idx-2, dp)
        notPick = 0 + self.maxRob(nums, idx-1, dp)
            
        dp[idx] = max(pick, notPick)
        
        return dp[idx]
            
    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        # return max(self.maxRob(nums[:n-1]), self.maxRob(nums[1:]))
        dp1 = [-1]*len(nums)
        dp2 = [-1]*len(nums)
        return max(self.maxRob(nums[:n-1], n-2, dp1), self.maxRob(nums[1:], n-2, dp2))
        
        
        