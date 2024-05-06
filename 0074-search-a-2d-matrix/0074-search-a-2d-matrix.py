class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i=0
        low = 0
        high = len(matrix[i]) - 1
        
        while i<len(matrix)-1:
            if target > matrix[i][high]:
                i += 1
            else:
                break
                
        while low <= high:
            mid = (low + high) // 2
            if target == matrix[i][mid]:
                return True
            elif target < matrix[i][mid]:
                high = mid - 1
            else:
                low = mid+1
        
        
            
                # mid = low + ((low - high)) //2
                
        return False
                
                
            