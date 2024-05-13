class Solution(object):

    # Recursion but TC - O(2^n)
    #     def nWays(self, n):
#         if n == 0:
#             return 1
#         elif n > 0:
#             return self.nWays(n-1) + self.nWays(n-2)
#         else:
#             return 0
    
    
    
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # return self.nWays(n)
        
        # Bottom up DP
        # TC - O(n), SC - O(1)
        one, two = 1, 1
        for _ in range(n-1):
            temp = one
            one = one + two
            two = temp
            
        return one
            
        
        