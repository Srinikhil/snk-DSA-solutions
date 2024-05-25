#User function Template for python3

class Solution:
    # def jumps(self, idx, dp, height, k):
        
    #     # Memoization approach TC - O(N*k), SC - O(N)+O(N)
    #     if idx == 0:
    #         return 0
    #     if dp[idx] != -1:
    #         return dp[idx]
        
    #     minkSteps = 99999
    #     # jump = 0
        
    #     for j in range(1, k+1):
    #         if idx >= j:
    #             jump = self.jumps(idx-j, dp, height, k) + abs(height[idx] - height[idx-j])
    #             minkSteps = min(minkSteps, jump)
        
    #     dp[idx] = minkSteps
                
    #     return dp[idx]
        
    
    def minimizeCost(self, height, n, k):
    # Memoization Approach
    #     dp = [-1]*n
    #     return self.jumps(n-1, dp, height, k)
        
        
        # Tabulation Approach TC - O(N*K), SC - O(N)
        dp = [0]*n
        
        jump = 0
        for i in range(1, n):
            minkSteps = 99999
            for j in range(1, k+1):
                if i >= j:
                    jump = dp[i-j] + abs(height[i]-height[i-j])
                    minkSteps = min(jump, minkSteps)
            dp[i] = minkSteps
            
        # print(dp)
        return dp[n-1]
                
        
