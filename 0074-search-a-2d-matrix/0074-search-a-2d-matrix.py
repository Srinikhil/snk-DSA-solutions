class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # TC - O(mlogn)
        
#         i=0
#         low = 0
#         high = len(matrix[i]) - 1
        
#         while i<len(matrix)-1:
#             if target > matrix[i][high]:
#                 i += 1
#             else:
#                 break
                
#         while low <= high:
#             mid = (low + high) // 2
#             if target == matrix[i][mid]:
#                 return True
#             elif target < matrix[i][mid]:
#                 high = mid - 1
#             else:
#                 low = mid+1
        
        
            
#                 # mid = low + ((low - high)) //2
                
#         return False


        # TC - O(log(m*n))
        vlow = 0
        vhigh = len(matrix) - 1
        
        hlow = 0
        hhigh = len(matrix[0]) - 1
        
        
        while vlow <= vhigh:
            vmid = (vlow+vhigh) // 2
            if target >= matrix[vmid][hlow] and target <= matrix[vmid][hhigh]:
                hmid = (hlow+hhigh) // 2
                if target == matrix[vmid][hmid]:
                    return True
                elif target < matrix[vmid][hmid]:
                    hhigh = hmid - 1
                else:
                    hlow = hmid+1
                    
            elif target < matrix[vmid][hlow]:
                vhigh = vmid-1
                    
            # elif target > matrix[vmid][hhigh]:
            else:
                vlow = vmid+1
                
        return False
                
                
                
            