class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        # Using Type conversion
#         x = str(x)
#         i = 0
#         j = len(x) - 1
#         while i <= j:
#             if x[i] != x[j]:
#                 return False
#             i += 1
#             j -= 1
            
#         return True

        
        # reverse string and compare
        # if x < 0:
        #     return False
        # else:
        #     x = str(x)
        #     if x != x[::-1]:
        #         return False
        #     return True
        
        
    # Approach - 2
        arr = []

        if x < 0:
            return False
        else:
            while x > 0:
                arr.append(x%10)
                x = x // 10
                
            i = 0
            j = len(arr) - 1
            while i <= j:
                if arr[i] != arr[j]:
                    return False
                i += 1
                j -= 1
                
            return True


    
        