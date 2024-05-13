class Solution(object):
    def sumOfSquares(self, n):
        nSquareSum = 0
        onesDigit = -1
        
        while n > 0:
            onesDigit = n%10
            nSquareSum += onesDigit**2
            n = n//10
        
        return nSquareSum
    
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        track = []
        while True:
            n = self.sumOfSquares(n)
            if n in track:
                break
            track.append(n)
            # print(n)
            
            
                
        print("final n", n)
        return True if n==1 else False