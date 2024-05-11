class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        expSum = (n * (n+1)) / 2
        arrSum = 0
        for i in nums:
            arrSum += i
        
        return expSum - arrSum