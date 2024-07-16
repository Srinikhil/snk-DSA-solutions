from typing import List
import sys

def minSubsetSumDifference(arr: List[str], n: int) -> int:
    # write your code here
    totSum = 0
    for i in range(n):
        totSum += arr[i]

    prev = [0]*(totSum+1)
    cur = [0]*(totSum+1)

    prev[0], cur[0] = True, True

    if arr[0] <= totSum:
        prev[arr[0]] = True

    for ind in range(1, n):
        for target in range(1, totSum+1):
            notTake = prev[target]
            take = False
            if target >= arr[ind]:
                take = prev[target-arr[ind]]
            cur[target] = take or notTake

        prev = cur.copy()

    S1 = -1 
    S2 = -1
    minDiff = sys.maxsize

    for i in range((totSum//2)+1):
        if prev[i] == True:
            S1 = i
            S2 = totSum - S1
            absDiff = abs(S1-S2)
            if absDiff < minDiff:
                minDiff = absDiff

    return minDiff
