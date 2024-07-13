from os import *
from sys import *
from collections import *
from math import *


# Recursion: TC - O(2^n), SC - O(n)
# def helper(arr, ind, target):
#     if target == 0:
#         return True
#     if ind == 0:
#         return arr[0] == target

#     notTake = helper(arr, ind-1, target)
#     take = False
#     if target >= arr[ind]:
#         take = helper(arr, ind-1, target-arr[ind])

#     return take or notTake
# 

# Memoization TC - O(n*k), SC - O(n*target)+O(n)
# def memoizedhelper(arr, ind, target, dp):
#     if target == 0:
#         return True
#     if ind == 0:
#         return arr[0] == target
#     if dp[ind][target] != -1:
#         return dp[ind][target]

#     notTake = memoizedhelper(arr, ind-1, target, dp)
#     take = False
#     if target >= arr[ind]:
#         take = memoizedhelper(arr, ind-1, target-arr[ind], dp)

#     dp[ind][target] = take or notTake

#     return dp[ind][target]



def subsetSumToK(n, k, arr):

    # Write your code here
    # Return a boolean variable 'True' or 'False' denoting the answer
    
    # Recursion
    # return helper(arr, n-1, k)

    # Memoization
    # dp = [[-1]*(k+1) for _ in range(n)]
    # return memoizedhelper(arr, n-1, k, dp)

    
    # Tabulation TC-O(n*target), SC-O(n*target)
    # dp = [[0]*(k+1) for _ in range(n)]

    # for i in range(0, n):
    #     dp[i][0] = True

    # if arr[0] <= k:
    #     dp[0][arr[0]] = True

    # for ind in range(1, n):
    #     for target in range(1, k+1):
    #         notTake = dp[ind-1][target]
    #         take = False
    #         if target >= arr[ind]:
    #             take = dp[ind-1][target-arr[ind]]

    #         dp[ind][target] = take or notTake

    # return dp[n-1][k]


    # Space Optimization TC-O(n*target), SC-O(2*target)

    prev = [0]*(k+1)
    cur = [0]*(k+1)

    prev[0], cur[0] = True, True

    if arr[0] <= k:
        prev[arr[0]] = True

    for ind in range(1, n):
        for target in range(1, k+1):
            notTake = prev[target]
            take = False
            if target >= arr[ind]:
                take = prev[target-arr[ind]]

            cur[target] = take or notTake

        prev = cur

    return prev[k]
