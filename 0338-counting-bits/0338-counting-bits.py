class Solution(object):
    
    # Bruteforce approach
#     def countOnes(self, num):
#         setBitCount = 0
#         while num > 0:
#             setBitCount += 1
#             num = num & (num - 1)
            
#         return setBitCount
    
    
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
#         bitCounts = []
#         for num in range(n+1):
#             bitCounts.append(self.countOnes(num))
            
#         return bitCounts


        bitCounts = [0]
        # latest2n = 0
        latest2n = 1
        
        for i in range(1, n+1):
            # To keep an offset at power of 2
            if i and (not (i & (i-1))):
            # if latest2n * 2 == i:
                bitCounts.append(1)
                latest2n = i
            else:
                # bitCounts.append(bitCounts[latest2n] + bitCounts[i - latest2n])
                bitCounts.append(bitCounts[i - latest2n]+1)

                
        return bitCounts