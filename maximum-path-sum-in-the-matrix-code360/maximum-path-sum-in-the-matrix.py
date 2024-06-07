from os import *
from sys import *
from collections import *
from math import *


from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)


# Memoization Approach TC - O(M*N + N)
# def fun(i, j, arr, dp):
    # if m and n are not equal unlike in quest
    # m = len(arr)
    # n = len(arr[0])
    # if j<0 or j>=n:
    #     return -9999999
    # if i == 0:
    #     return arr[i][j]
    # if dp[i][j] != -1:
    #     return dp[i][j]
    
    # s = arr[i][j] + fun(i-1, j, arr, dp)
    # ld = arr[i][j] + fun(i-1, j-1, arr, dp)
    # rd = arr[i][j] + fun(i-1, j+1, arr, dp)
    
    # dp[i][j] = max(s, ld, rd)
    
    # return dp[i][j]

def getMaxPathSum(matrix):

    #   Write your code here
    # m = len(matrix)
    # n = len(matrix[0])
    
    # # dp = [[-1]*n for _ in range(n)]
    # dp = [[-1]*n for _ in range(m)]
    
    # maxi = -99999999999
    # for j in range(n):
    #     maxi = max(maxi, fun(m-1, j, matrix, dp))
        
    # return maxi

    # Tabulation approach TC (M*N + N), SC - O(M*N)
    m = len(matrix)
    n = len(matrix[0])

    # dp = [[0]*n for _ in range(m)]

    # for j in range(n):
    #     dp[0][j] = matrix[0][j]
    

    # for i in range(1, m):

    #     for j in range(n):
    #         s, ld, rd = -9999999, -9999999, -9999999
    #         s = matrix[i][j] + dp[i-1][j]
    #         if j > 0:
    #             ld = matrix[i][j] + dp[i-1][j-1]
    #         if j < n-1:
    #             rd = matrix[i][j] + dp[i-1][j+1]

    #         dp[i][j] = max(s, ld, rd)

    # maxi = dp[m-1][0]
    # for j in range(1, n):
    #     maxi = max(maxi, dp[m-1][j])
    
    # return maxi

    # Space Optimization Approach TC - O(M*N + N), SC - O(2N)

    prev = [0]*n

    for j in range(n):
        prev[j] = matrix[0][j]

    for i in range(1, m):
        cur = [0]*n
        for j in range(n):
            ld, rd = -9999999, -9999999
            s = matrix[i][j] + prev[j]
            if j>0:
                ld = matrix[i][j] + prev[j-1]
            if j<n-1:
                rd = matrix[i][j] + prev[j+1]

            cur[j] = max(s, ld, rd)
        
        prev = cur



    return max(prev)

        
    
        


























#   taking inpit using fast I/O
def takeInput() :
    n_x = stdin.readline().strip().split(" ")
    n = int(n_x[0].strip())
    m = int(n_x[1].strip())

    matrix=[list(map(int, stdin.readline().strip().split(" "))) for row in range(n)]

    return matrix, n, m


#   main
T = int(input())
while (T > 0):
    T -= 1
    matrix, n, m = takeInput()
    print(getMaxPathSum(matrix))
