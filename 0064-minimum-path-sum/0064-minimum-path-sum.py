import sys

class Solution(object):
    def pathFun(self, i, j, arr, dp):
        if i == 0 and j == 0:
            return arr[i][j]
        if i < 0 or j < 0:
            return sys.maxint
        if dp[i][j] != -1:
            return dp[i][j]
        
        up = arr[i][j] + self.pathFun(i-1, j, arr, dp)
        left = arr[i][j] + self.pathFun(i, j-1, arr, dp)
        
        dp[i][j] = min(up, left)
        return dp[i][j]
    
    
    
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        
        dp = [[-1]*n for _ in range(m)]
        
        return self.pathFun(m-1, n-1, grid, dp)