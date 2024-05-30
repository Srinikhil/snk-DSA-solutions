class Solution(object):
#     def countPaths(self, i, j, arr, dp):
        
#         # Memoization approach TC - O(M*N) SC - O((M-1)+(N-1)+(M*N))
#         if i>=0 and j>=0 and arr[i][j] == 1:
#             return 0
#         if i==0 and j==0:
#             return 1
#         if i<0 or j<0:
#             return 0
#         if dp[i][j] != -1:
#             return dp[i][j]
        
#         up, left = 0, 0
#         if i>0:
#             up = self.countPaths(i-1, j, arr, dp)
#         if j>0:
#             left = self.countPaths(i, j-1, arr, dp)
            
#         dp[i][j] = up+left
#         return dp[i][j]
        
    
    
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        # Memoization Approach
#         dp = [[-1]*len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        
#         m = len(obstacleGrid)
#         n = len(obstacleGrid[0])
#         return self.countPaths(m-1, n-1, obstacleGrid, dp)


        # Tabulation TC - O(M*N), SC - O(M*N)
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
#         dp = [[0]*n for _ in range(m)]
#         # print(dp)
        
#         for i in range(m):
#             for j in range(n):
#                 if obstacleGrid[i][j] == 1:
#                     pass
#                 elif i == 0 and j == 0:
#                     dp[i][j] = 1
#                 # if i == 0 and j == 0 and obstacleGrid[i][j] != 1:
#                 #     dp[i][j] = 1
#                 # elif obstacleGrid[i][j] != 1:
#                 else:
#                     up, left = 0, 0
#                     if i>0:
#                         up = dp[i-1][j]
#                     if j>0:
#                         left = dp[i][j-1]
#                     # print("up+left",up+left)
#                     dp[i][j] = up+left
#                     # print("i", i, "j", j, "dp-->", dp)
#         return dp[m-1][n-1]


        # Space Optimization TC - O(M*N), SC - O(2N) [which is O(N)]
        prev = [0]*n
        for i in range(m):
            cur = [0]*n
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    pass
                elif i == 0 and j == 0:
                    cur[j] = 1
                else:
                    # up, left = 0, 0
                    # if i>0:
                    #     up = prev[j]
                    # if j>0:
                    #     left = cur[j-1]
                    # cur[j] = up+left
                    # computing with one step left and one step up
                    
                    cur[j] = prev[j] + cur[j-1]
                    
            prev = cur
            
        return prev[n-1]
                    
        
        
        