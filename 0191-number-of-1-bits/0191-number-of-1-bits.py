class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        setBitCount = 0
        while n >= 1:
            if n % 2 == 1:
                setBitCount += 1
            n = n // 2
            
        return setBitCount