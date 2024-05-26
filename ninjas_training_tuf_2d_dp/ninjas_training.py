from typing import *

# def fun(idx: int, last: int, points: List[List[int]], dp: List[List[int]]) -> int:
    
    # Recursion Approach
    # maxi = 0
    # if idx == 0:
    #     for i in range(3):
    #         if i != last:
    #             maxi = max(maxi, points[idx][i])
    # else:
    #     curPoints = 0
    #     for i in range(3):
    #         if i != last:
    #             curPoints = points[idx][i] + fun(idx-1, i, points)
    #             maxi = max(maxi, curPoints)

    # return maxi


    # Memoization Approach TC - O(N*4*3), SC - O(N) + O(N*4)
    # maxi = 0
    # if idx == 0:
    #     for i in range(3):
    #         if i != last:
    #             maxi = max(maxi, points[idx][i])
    #     dp[idx][last] = maxi
    #     return dp[idx][last]

    # elif dp[idx][last] != -1:
    #     return dp[idx][last]
    
    # else:
    #     curPoints = 0
    #     for i in range(3):
    #         if i != last:
    #             curPoints = points[idx][i] + fun(idx-1, i, points, dp)
    #             maxi = max(maxi, curPoints)

    #     dp[idx][last] = maxi
    #     return dp[idx][last]
        


  
def ninjaTraining(n: int, points: List[List[int]]) -> int:

    # Write your code here.
    # Recursion Approach
    # return fun(n-1, 3, points)

    # Memoization Approach
    # dp = [[-1]*4 for _ in range(n)]
    # return fun(n-1, 3, points, dp)

    # Tabulation Approach TC - O(N*4*3), SC - O(N*4)

    # dp = [[0]*4 for _ in range(n)]

    # # dp[0][0] = max(points[0][1], points[0][2])
    # # dp[0][1] = max(points[0][0], points[0][2])
    # # dp[0][2] = max(points[0][0], points[0][1])
    # # dp[0][3] = max(points[0][0], points[0][1], points[0][2])

    # # for day in range(1, n):
    
    # for day in range(0, n):
    #     for last in range(4):
    #         maxi = 0
    #         curpoints = 0
    #         for task in range(3):
    #             if task != last:
    #                 curpoints = points[day][task] + dp[day-1][task]
    #                 maxi = max(maxi, curpoints)
    #         dp[day][last] = maxi

    # return dp[n-1][3]


    # Space Optimization TC - O(N*4*3), SC - O(4)
    prev = [0]*4

    prev[0] = max(points[0][1], points[0][2])
    prev[1] = max(points[0][0], points[0][2])
    prev[2] = max(points[0][0], points[0][1])
    prev[3] = max(points[0][0], points[0][1], points[0][2])
    
    
    for day in range(1, n):
        temp = [0]*4
        for last in range(4):
            curpoints = 0
            for task in range(3):
                if task != last:
                    curpoints = points[day][task] + prev[task]
                    temp[last] = max(temp[last], curpoints)

        prev = temp


    return prev[3]
