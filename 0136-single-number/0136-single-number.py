class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #TC - O(n), SC - O(n)
        
#         freqDict = {}
#         for n in nums:
#             if n in freqDict:
#                 freqDict[n] += 1
#             else:
#                 freqDict[n] = 1

#         for i in freqDict:
#             if freqDict[i] < 2:
#                 return i

        # But only constant extra space can be used.

        # using XOR this can be done, all elements which appeared twice cancelout leaving the required one.
        
        r = 0
        for n in nums:
            r = r ^ n
            
        return r
    
        
        