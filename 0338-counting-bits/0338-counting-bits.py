class Solution(object):
    def countOnes(self, num):
        setBitCount = 0
        while num > 0:
            setBitCount += 1
            num = num & (num - 1)
            
        return setBitCount
    
    
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        bitCounts = []
        for num in range(n+1):
            bitCounts.append(self.countOnes(num))
            
        return bitCounts
        