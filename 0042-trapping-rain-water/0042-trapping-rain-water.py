class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
#         lh = 0
#         rh = 1
#         trappedWater = 0
#         temp_rh = 0
        
#         while lh < len(height):
#             while rh < len(height):

#                 if height[rh] >= height[lh]:
#                     temp_rh = rh-1
#                     while temp_rh > lh:
#                         trappedWater += height[lh] - height[temp_rh]
#                         temp_rh -= 1
#                     lh = rh
#                     rh += 1
#                 rh += 1
#             lh += 1
#             rh = lh + 1

#         return trappedWater

#         trappedWater = 0
#         # Bruteforce approach
#         for i in range(len(height)):
#             lmax = 0
#             rmax = 0
#             for l in range(0, i+1):
#                 if height[l] > lmax:
#                     lmax = height[l]
#             for r in range(i, len(height)):
#                 if height[r] > rmax:
#                     rmax = height[r]
                
                
#             trappedWater += min(lmax, rmax) - height[i]
            
#         return trappedWater

        trappedWater = 0
        lh = 0
        rh = len(height) - 1
        lmax = height[lh]
        rmax = height[rh]
        
        while lh <= rh:
            if height[lh] <= height[rh]:
                if height[lh] > lmax:
                    lmax = height[lh]
                else:
                    trappedWater += lmax - height[lh]
                lh += 1
                    
            else:
                if height[rh] > rmax:
                    rmax = height[rh]
                else:
                    trappedWater += rmax - height[rh]
                rh -= 1
                
        return trappedWater