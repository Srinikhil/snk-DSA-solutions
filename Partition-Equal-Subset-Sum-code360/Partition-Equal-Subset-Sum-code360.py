def subSetSum(k, n, arr):
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

        prev = cur.copy()

    return prev[k]



def canPartition(arr, n):
    # Write your code here.
    totSum = 0
    for i in range(n):
        totSum += arr[i]

    if (totSum % 2):
        return False

    target = totSum//2
    
    return subSetSum(target, n, arr)
