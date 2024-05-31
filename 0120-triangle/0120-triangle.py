class Solution(object):
    # Memoization Approach TC - O(N*N), SC - O(N)+O(N*N)
#     def pathFun(self, i, j, triangle, dp):
#         n = len(triangle)
#         if i == n-1:
#             return triangle[i][j]
#         if dp[i][j] != -1:
#             return dp[i][j]
        
#         down = triangle[i][j] + self.pathFun(i+1, j, triangle, dp)
#         diag = triangle[i][j] + self.pathFun(i+1, j+1, triangle, dp)
        
#         dp[i][j] = min(down, diag)
#         return dp[i][j]
    
    
    
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # Memoization Approach
#         n = len(triangle)
#         dp = [[-1]*n for _ in range(n)]
        
#         return self.pathFun(0, 0, triangle, dp)

        # Tabulation TC - O(N*N), SC - O(N*N)
#         n = len(triangle)
#         dp = [[0]*n for _ in range(n)]
        
#         # Base Case
#         for j in range(n):
#             dp[n-1][j] = triangle[n-1][j]
            
#         for i in range(n-2, -1, -1):
#             for j in range(i, -1, -1):
#                 down = triangle[i][j] + dp[i+1][j]
#                 diag = triangle[i][j] + dp[i+1][j+1]
#                 dp[i][j] = min(down, diag)
                
#         return dp[0][0]
    
    
    
        # Space Optimization TC - O(N*N), SC - O(N)
        n = len(triangle)
        next = [0]*n
        
        # Base Case
        for j in range(n):
            next[j] = triangle[n-1][j]
            
        for i in range(n-2, -1, -1):
            cur = [0]*(i+1)
            for j in range(i, -1, -1):
                down = triangle[i][j] + next[j]
                diag = triangle[i][j] + next[j+1]
                cur[j] = min(down, diag)
            next = cur
                
        return next[0]
        
        
        