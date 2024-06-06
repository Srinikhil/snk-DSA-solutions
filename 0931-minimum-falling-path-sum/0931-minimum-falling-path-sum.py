class Solution(object):
    
    # Memoization Approach
#     def fun(self, i, j, arr, dp):
#         # if m and n are not equal unlike in quest
#         # m = len(arr)
#         n = len(arr[0])
#         if j<0 or j>=n:
#             return sys.maxint
#         if i == 0:
#             return arr[i][j]
#         if dp[i][j] != -1:
#             return dp[i][j]
        
#         s = arr[i][j] + self.fun(i-1, j, arr, dp)
#         ld = arr[i][j] + self.fun(i-1, j-1, arr, dp)
#         rd = arr[i][j] + self.fun(i-1, j+1, arr, dp)
        
#         dp[i][j] = min(s, ld, rd)
        
#         return dp[i][j]
    
    
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # m = len(matrix)
#         n = len(matrix[0])
        
#         dp = [[-1]*n for _ in range(n)]
#         # dp = [[-1]*n for _ in raneg(m)]
        
#         mini = sys.maxint
#         for j in range(n):
#             mini = min(mini, self.fun(n-1, j, matrix, dp))
            
#         return mini

        # Tabulation Approach TC - O(MxN + N), SC - O(MxN)
        n = len(matrix)
#         dp = [[0]*n for _ in range(n)]
        
#         for j in range(n):
#             dp[0][j] = matrix[0][j]
            
#         for i in range(1, n):
#             for j in range(n):
#                 ld, rd = sys.maxint, sys.maxint
#                 s = matrix[i][j] + dp[i-1][j]
#                 if j>0:
#                     ld = matrix[i][j] + dp[i-1][j-1]
#                 if j<n-1:
#                     rd = matrix[i][j] + dp[i-1][j+1]
#                 dp[i][j] = min(s, ld, rd)
                
#         mini = dp[n-1][0]
#         for j in range(1, n):
#             mini = min(mini, dp[n-1][j])
            
    
    
        # Space Optimization TC - O(MxN + N), SC - O(2N)
        prev = [0]*n
        
        for j in range(n):
            prev[j] = matrix[0][j]
            
        for i in range(1, n):
            # print(prev, "i-->", i)
            cur = [0]*n
            for j in range(n):
                ld, rd = sys.maxint, sys.maxint
                s = matrix[i][j] + prev[j]
                if j>0:
                    ld = matrix[i][j] + prev[j-1]
                if j<n-1:
                    rd = matrix[i][j] + prev[j+1]
                cur[j] = min(s, ld, rd)
                # print(cur, "cur<--", "i-->", i)
            prev = cur
            
    
        # print(prev)            
        mini = min(prev)
            
            
        return mini
                
        