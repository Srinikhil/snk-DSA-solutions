class Solution(object):
    # Memoization Approach TC - O(N), SC - O(N)+O(N*N)
    def pathFun(self, i, j, triangle, dp):
        n = len(triangle)
        if i == n-1:
            return triangle[i][j]
        if dp[i][j] != -1:
            return dp[i][j]
        
        down = triangle[i][j] + self.pathFun(i+1, j, triangle, dp)
        diag = triangle[i][j] + self.pathFun(i+1, j+1, triangle, dp)
        
        dp[i][j] = min(down, diag)
        return dp[i][j]
    
    
    
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        dp = [[-1]*n for _ in range(n)]
        
        return self.pathFun(0, 0, triangle, dp)
        
        