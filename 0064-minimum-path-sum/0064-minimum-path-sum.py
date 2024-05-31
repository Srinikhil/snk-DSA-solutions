import sys

class Solution(object):
    # Memoization Approach
#     def pathFun(self, i, j, arr, dp):
#         if i == 0 and j == 0:
#             return arr[i][j]
#         if i < 0 or j < 0:
#             return sys.maxint
#         if dp[i][j] != -1:
#             return dp[i][j]
        
#         up = arr[i][j] + self.pathFun(i-1, j, arr, dp)
#         left = arr[i][j] + self.pathFun(i, j-1, arr, dp)
        
#         dp[i][j] = min(up, left)
#         return dp[i][j]
    
    
    
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        
        # Memoization Approach
        # dp = [[-1]*n for _ in range(m)]
        # return self.pathFun(m-1, n-1, grid, dp)
        
        # Tabulation Approach
        dp = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                else:
                    up, left = sys.maxint, sys.maxint
                    if i>0:
                        up = grid[i][j] + dp[i-1][j]
                    if j>0:
                        left = grid[i][j] + dp[i][j-1]
                    
                    dp[i][j] = min(up,left)
                    # print("i", i, "j", j, "dp-->", dp)
                    
        return dp[m-1][n-1]