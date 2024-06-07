from os import *
from sys import *
from collections import *
from math import *

from typing import List


# Memoization Approach - TC O(NxMxM)x9, SC - O(NxMxM) + O(N)
# def fun(r: int, c: int, i: int, j1: int, j2: int, arr: List[List[int]], dp: List[List[List[int]]]):
#     if j1<0 or j1>c-1 or j2<0 or j2>c-1:
#         return -1e8
    
#     if i == r-1:
#         if j1 == j2:
#             return arr[i][j1]
#         else:
#             return arr[i][j1] + arr[i][j2]

#     if dp[i][j1][j2] != -1:
#         return dp[i][j1][j2]
    
#     maxi = -1e8
#     for dj1 in range(-1, 2):
#         for dj2 in range(-1, 2):
#             if j1 == j2:
#                 maxi = max(maxi, arr[i][j1] + fun(r, c, i+1, j1+dj1, j2+dj2, arr, dp))
#             else:
#                 maxi = max(maxi, arr[i][j1]+ arr[i][j2] + fun (r, c, i+1, j1+dj1, j2+dj2, arr, dp))

#     return maxi



def maximumChocolates(r: int, c: int, grid: List[List[int]]) -> int:
    # write your code here

    # Memoization Approach
    # dp = [[[-1]*c for _ in range(c)] for _ in range(r)]
    # return (fun(r, c, 0, 0, c-1, grid, dp))
    
    # Tabulation Approach TC - O(NxMxM)x9, SC - O(NxMxM)
    # dp = [[[0]*c for _ in range(c)] for _ in range(r)]

    # for j1 in range(c):
    #     for j2 in range(c):
    #         if j1 == j2:
    #             dp[r-1][j1][j2] = grid[r-1][j1]
    #         else:
    #             dp[r-1][j1][j2] = grid[r-1][j1] + grid[r-1][j2]

    # for i in range(r-2, -1, -1):
    #     for j1 in range(c):
    #         for j2 in range(c):
    #             maxi = -1e8
    #             for dj1 in range(-1, 2):
    #                 for dj2 in range(-1, 2):

    #                     if j1+dj1<0 or j1+dj1>c-1 or j2+dj2<0 or j2+dj2>c-1:
    #                         dp[i][j1][j2] = -1e8
    #                     else:
    #                         if j1 == j2:
    #                             maxi = max(maxi, grid[i][j1]+dp[i+1][j1+dj1][j2+dj2])
    #                         else:
    #                             maxi = max(maxi, grid[i][j1]+grid[i][j2]+dp[i+1][j1+dj1][j2+dj2])

    #             #         value = 0
    #             #         if j1 == j2:
    #             #             value = grid[i][j1]
    #             #         else:
    #             #             value = grid[i][j1] + grid[i][j2]
    #             #         if j1+dj1<0 or j1+dj1>c-1 or j2+dj2<0 or j2+dj2>c-1:
    #             #             value += -1e8
    #             #         else:
    #             #             value += dp[i+1][j1+dj1][j2+dj2]
    #             #         maxi = max(maxi, value)

    #             dp[i][j1][j2] = maxi

    

    # return dp[0][0][c-1]


    # Space Optimization TC - O(NxMxM)x9, SC - O(MxM)
    front = [[0]*c for _ in range(c)]

    for j1 in range(c):
        for j2 in range(c):
            if j1 == j2:
                front[j1][j2] = grid[r-1][j1]
            else:
                front[j1][j2] = grid[r-1][j1] + grid[r-1][j2]

    for i in range(r-2, -1, -1):
        cur = [[0]*c for _ in range(c)]
        for j1 in range(c):
            for j2 in range(c):
                maxi = -1e8
                for dj1 in range(-1, 2):
                    for dj2 in range(-1, 2):

                        if j1+dj1<0 or j1+dj1>c-1 or j2+dj2<0 or j2+dj2>c-1:
                            cur[j1][j2] = -1e8
                        else:
                            if j1 == j2:
                                maxi = max(maxi, grid[i][j1]+front[j1+dj1][j2+dj2])
                            else:
                                maxi = max(maxi, grid[i][j1]+grid[i][j2]+front[j1+dj1][j2+dj2])

                #         value = 0
                #         if j1 == j2:
                #             value = grid[i][j1]
                #         else:
                #             value = grid[i][j1] + grid[i][j2]
                #         if j1+dj1<0 or j1+dj1>c-1 or j2+dj2<0 or j2+dj2>c-1:
                #             value += -1e8
                #         else:
                #             value += dp[i+1][j1+dj1][j2+dj2]
                #         maxi = max(maxi, value)

                cur[j1][j2] = maxi
        front = cur

    

    return front[0][c-1]


