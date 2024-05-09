class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #TC - O(n), SC - O(n)
        
        freqDict = {}
        for n in nums:
            if n in freqDict:
                freqDict[n] += 1
            else:
                freqDict[n] = 1

        for i in freqDict:
            if freqDict[i] < 2:
                return i
        
        