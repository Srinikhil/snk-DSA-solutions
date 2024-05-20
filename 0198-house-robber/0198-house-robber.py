class Solution(object):
    
    def rf(self, idx, nums, dp):
        if idx == 0:
            return nums[idx]
        if idx < 0:
            return 0
        if dp[idx] != -1:
            return dp[idx]
        
        pick = nums[idx] + self.rf(idx-2, nums, dp)
        notPick = 0 + self.rf(idx-1, nums, dp)
        
        dp[idx] = max(pick, notPick)
        return dp[idx]
    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Recursion: TC - O(2^N), SC - O(N)
        # n = len(nums)
        # return self.rf(n-1, nums)
        
        
        
        dp = [-1]*len(nums)

        n = len(nums)
        return self.rf(n-1, nums, dp)