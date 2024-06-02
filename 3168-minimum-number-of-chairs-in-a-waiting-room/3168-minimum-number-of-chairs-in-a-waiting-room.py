class Solution(object):
    def minimumChairs(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        maxChairs = 0
#         chairStack = []
        
#         for ch in s:
#             if ch == 'E':
#                 chairStack.append(ch)
#                 if len(chairStack) > maxChairs:
#                     maxChairs = len(chairStack)
                    
#             elif ch == 'L':
#                 chairStack.pop()
                
#         return maxChairs

        curChairs = 0
        
        for ch in s:
            if ch == 'E':
                curChairs += 1
                if curChairs > maxChairs:
                    maxChairs = curChairs
                
            elif ch == 'L':
                curChairs -= 1
                
        return maxChairs
        
