from os import *
from sys import *
from collections import *
from math import *

from typing import *

# def jumps(idx: int, dp: List[int], heights: List[int]) -> int:
#     twoSteps = 1001
#     if idx == 0:
#         return 0
#     if dp[idx] != -1:
#         return dp[idx]
#     oneStep = abs(heights[idx] - heights[idx-1]) + jumps(idx-1, dp, heights)
#     if idx > 1:
#         twoSteps = abs(heights[idx] - heights[idx-2]) + jumps(idx-2, dp, heights)

#     dp[idx] = min(oneStep, twoSteps)
#     return dp[idx]
  
def frogJump(n: int, heights: List[int]) -> int:

    # Write your code here.
    # For Recursive approach TC - O(2^N), SC - O(N)
    # Memoization Approach TC - O(N), SC - O(2N)
    # dp = [-1]*len(heights)
    # return jumps(n-1, dp, heights)

    # Tabulation Approach, TC - O(N), SC - O(N)
    # dp = [0]*(len(heights))
    # for i in range(1, len(heights)):
    #     twoStep = 1001
    #     oneStep = abs(heights[i]-heights[i-1])+dp[i-1]
    #     if i > 1:
    #         twoStep = abs(heights[i]-heights[i-2])+dp[i-2]
    #     dp[i] = min(oneStep, twoStep)

    # return dp[-1]

    # Space Optimiaztion TC - O(N), SC - O(1)
    dp = [0]*(len(heights))
    prev2, prev = 0, 0
    for i in range(1, len(heights)):
        # it is taken to be largest as in the first iteration we only need to take oneStep
        twoStep = 1001
        oneStep = abs(heights[i]-heights[i-1])+prev
        if i > 1:
            twoStep = abs(heights[i]-heights[i-2])+prev2
        prev2 = prev
        prev = min(oneStep, twoStep)

    return prev
