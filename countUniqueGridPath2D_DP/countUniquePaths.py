from collections import *
from math import *

# def countPaths(i, j, dp):
	# Memoization Approach TC - O(M*N), SC - O((M-1)+(N-1)+(M*N))
	# if i == 0 and j == 0:
	# 	return 1
	# if i<0 or j<0:
	# 	return 0
	# if dp[i][j] != -1:
	# 	return dp[i][j]

	# up = countPaths(i-1, j, dp)
	# left = countPaths(i, j-1, dp)
	# dp[i][j] = up+left

	# return dp[i][j]

def uniquePaths(m, n):
	# Write your code here.

	# Memoization Approach
	# dp = [[-1]*n for _ in range(m)]
	# return countPaths(m-1, n-1, dp)


	# Tabulation Approach TC - O(M*N), SC - O(M*N)
	# Auxilary stack space is omitted
	# dp = [[0]*n for _ in range(m)]
	# for i in range(m):
	# 	for j in range(n):
	# 		if i == 0 and j == 0:
	# 			dp[i][j] = 1
	# 		else:
	# 			up, left = 0, 0
	# 			if i>0:
	# 				up = dp[i-1][j]
	# 			if j>0:
	# 				left = dp[i][j-1]
	# 			dp[i][j] = up+left

	# return dp[m-1][n-1]


	# Space Optimization  TC - O(M*N) SC - O(N)
	prevRow = [0]*n

	for i in range(m):
		cur = [0]*n
		for j in range(n):
			if i == 0 and j == 0:
				cur[j] = 1
			else:
				# up, left = 0, 0
				# if i>0:
				# 	up = prevRow[j]
				# if j > 0:
				# 	left = cur[j-1]
				# cur[j] = up + left
				cur[j] = prevRow[j] + cur[j-1]

		prevRow = cur

	return prevRow[n-1]
